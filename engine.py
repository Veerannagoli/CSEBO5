import io
import re
import json
import nltk
import torch
import os
import pickle
import pandas as pd
from PyPDF2 import PdfReader
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from sentence_transformers import SentenceTransformer, util
from rank_bm25 import BM25Okapi
from groq import Groq

class ResumeRankingEngine:
    def __init__(self, groq_api_key: str):
        self.client = Groq(api_key=groq_api_key)
        self.model_id = "llama-3.1-8b-instant"
        self.embedder = SentenceTransformer("all-mpnet-base-v2")
        self.stop_words = set(stopwords.words('english'))
        
        # 1. LOAD THE LOCAL ML MODEL (NexusRole)
        try:
            with open('nexus_model.pkl', 'rb') as f:
                self.ml_model = pickle.load(f)
            with open('nexus_tfidf.pkl', 'rb') as f:
                self.tfidf = pickle.load(f)
            self.ml_ready = True
            print("✅ NexusRole ML Model Loaded.")
        except Exception as e:
            self.ml_ready = False
            print(f"⚠️ ML Model files not found: {e}")

        # 2. LOAD CSV DATASET (For Deep Reasoning)
        try:
            self.dataset = pd.read_csv("job_database.csv")
            self.role_list = self.dataset.to_dict(orient='records')
        except:
            self.role_list = []

    def clean_text_ml(self, text):
        """Standard cleaning for ML classification"""
        text = re.sub(r'http\S+\s*', ' ', text)
        text = re.sub(r'RT|cc', ' ', text)
        text = re.sub(r'#\S+', '', text)
        text = re.sub(r'@\S+', '  ', text)
        text = re.sub(r'[%s]' % re.escape("""!"#$%&'()*+,-./:;<=>?@[\]^_`{|}~"""), ' ', text)
        text = re.sub(r'[^\x00-\x7f]',r' ', text) 
        text = re.sub(r'\s+', ' ', text)
        return text.lower().strip()

    def predict_role_ml(self, text):
        """Instant prediction using the Support Vector Machine (SVM)"""
        if not self.ml_ready: return "Technical Professional"
        cleaned = self.clean_text_ml(text)
        vec = self.tfidf.transform([cleaned])
        return self.ml_model.predict(vec)[0]

    def _get_text_from_pdf(self, path):
        try:
            reader = PdfReader(path)
            return "".join(page.extract_text() or "" for page in reader.pages)
        except: return ""

    def _bm25_score(self, corpus_text, query_text):
        def tokenize(t):
            return [w for w in word_tokenize(str(t).lower()) if w.isalnum() and w not in self.stop_words]
        t_corpus = [tokenize(corpus_text)]
        t_query = tokenize(query_text)
        if not t_corpus[0] or not t_query: return 0.0
        bm25 = BM25Okapi(t_corpus)
        return min(bm25.get_scores(t_query)[0] / (len(t_query) + 1), 1.0)

    def score_single_resume(self, path, jd_text, jd_emb, level):
        raw_text = self._get_text_from_pdf(path)
        
        # 1. ML CATEGORY PREDICTION (Fast baseline)
        ml_category = self.predict_role_ml(raw_text)
        
        # 2. HYBRID SCORING (Safety Net + 1.55 Boost)
        full_sem = util.cos_sim(self.embedder.encode(raw_text, convert_to_tensor=True), jd_emb).item()
        full_lex = self._bm25_score(raw_text, jd_text)
        combined_raw = (0.7 * full_sem) + (0.3 * full_lex)
        
        final_score = min(combined_raw * 1.55, 1.0)
        
        category_label = "Excellent Fit" if final_score >= 0.70 else \
                         "Moderate Fit" if final_score >= 0.50 else \
                         "Weak Fit" if final_score >= 0.35 else "Poor Fit"
                   
        return {
            "score": round(float(final_score), 4),
            "category": category_label,
            "filename": os.path.basename(path),
            "predicted_role": ml_category # This will show the Category on the dashboard
        }

    def generate_deep_report(self, path, jd_text):
        raw_text = self._get_text_from_pdf(path)
        resume_text = self.clean_text_ml(raw_text)
        ml_role = self.predict_role_ml(raw_text)
        dataset_context = json.dumps(self.role_list[:15]) 

        prompt = f"""
        Act as a Senior HR Tech Lead. 
        RESUME: {resume_text[:4000]}
        
        TASK:
        1. Extract the CANDIDATE'S ACTUAL FULL NAME from the top of the resume.
        2. Identify specific matched technologies and skill gaps.
        3. Use this ML Hint: {ml_role} to find the best title in this DATABASE: {dataset_context}

        Return ONLY JSON:
        {{
          "candidate_name": "REAL_NAME_HERE",
          "best_match": "JOB_TITLE",
          "matched_skills": ["s1", "s2"],
          "reasoning": "Technical justification.",
          "skill_gaps": ["g1", "g2"],
          "recommended": "Certifications",
          "alternatives": ["Alt 1"]
        }}
        """
        response = self.client.chat.completions.create(
            model=self.model_id,
            response_format={"type": "json_object"},
            messages=[{"role": "user", "content": prompt}],
            temperature=0.1
        )
        return json.loads(response.choices[0].message.content)

    def rank_resumes(self, paths, jd_text, level):
        jd_emb = self.embedder.encode(jd_text, convert_to_tensor=True)
        results = [self.score_single_resume(p, jd_text, jd_emb, level) for p in paths]
        return sorted(results, key=lambda x: x['score'], reverse=True)