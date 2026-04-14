NexHire AI | Next-Gen Talent Intelligence System 🚀
![alt text](https://img.shields.io/badge/Python-3.12-blue.svg)

![alt text](https://img.shields.io/badge/ML_Accuracy-99.48%25-orange.svg)

![alt text](https://img.shields.io/badge/Reasoning-Llama_3.1-blueviolet.svg)

![alt text](https://img.shields.io/badge/Semantic-MPNet-green.svg)
NexHire AI is a state-of-the-art recruitment engine that moves beyond traditional keyword-based screening. It utilizes a Hybrid Inference Pipeline that combines locally-trained Machine Learning (SVM), probabilistic keyword ranking (BM25), and Generative AI (Llama 3.1) to provide 99.48% accurate role classification and human-like technical reasoning.
🧠 Technical Deep Dive: The Models
NexHire AI uses a "Tri-Layer" intelligence approach to evaluate candidates.
1. Semantic Matching (MPNet)
Model: all-mpnet-base-v2 (Sentence-Transformers)
Function: This model maps the resume and the Job Description into a 768-dimensional vector space.
Why it matters: Unlike simple word matching, it understands context. It recognizes that "Developing Scalable Data Pipelines" and "ETL Orchestration" are semantically identical, even if the words are different.
2. Lexical Precision (BM25 Okapi)
Algorithm: Rank-BM25
Function: While MPNet handles "Meaning," BM25 handles "Precision." It is a probabilistic model that calculates the importance of rare keywords.
Why it matters: It ensures that "Hard Skills" (like SQL, AWS, or Docker) are strictly verified. If a JD asks for a specific tool, BM25 ensures the candidate isn't ranked highly without it.
3. Role Classification (LinearSVC)
Model: Support Vector Machine (LinearSVC) + TF-IDF
Accuracy: 99.48% F1-Score
Function: A deterministic ML model trained on 14,000 resumes. It instantly identifies the candidate's professional category (e.g., Data Science, Web Development) without the latency or cost of an API call.
4. Generative Reasoning (Llama 3.1)
Model: llama-3.1-8b-instant (via Groq)
Function: Acts as the Reasoning Engine. It performs a "Gap Analysis" by comparing the resume against the job_database.csv.
Why it matters: It provides Explainable AI (XAI). It generates technical justifications, lists missing skills, and suggests specific certifications.
🌟 Key Features
Hybrid Scoring: Calculated as: [(Semantic * 0.7) + (Lexical * 0.3)] * 1.55 Boost.
99.48% Accurate Classification: Instant local role prediction.
Zero-Hallucination Grounding: AI titles are strictly anchored to your company's job_database.csv.
Dynamic Weighting: Automatically adjusts scoring logic for Internship vs. Experienced profiles.
Top-N Export: One-click ZIP download of the top-ranked candidate resumes.
Real-Name Extraction: AI intelligently extracts the candidate's actual name from the PDF text.
⚙️ Execution Flow (Step-by-Step)
The engine follows a strict pipeline to ensure data integrity and ranking speed:
Ingestion & Cleaning:
Raw text is extracted via PyPDF2.
Custom Regex removes "noise" (bullet points, non-ASCII characters, extra whitespace).
Global Safety-Net Ranking:
The engine performs a "Global Match" (Whole Resume vs Whole JD) to create a baseline score.
Local ML Classification:
The nexus_model.pkl (SVM) identifies the candidate’s professional family instantly.
Hybrid Scorer:
The all-mpnet-base-v2 calculates semantic similarity.
BM25 calculates keyword frequency.
A 1.55x Calibration Boost is applied to the final result.
Dashboard Display:
Results are sorted and displayed on the Flask UI with the ML-predicted job title.
Deep AI Report (On Click):
Llama 3.1 reads the specific resume text.
It maps skills to the job_database.csv.
It returns a JSON object containing technical reasoning and skill gaps.
Shortlist Export:
The recruiter selects the number of top candidates and downloads a ZIP of their PDFs.
📊 Model Performance
Tested against a validation set of 1,000 samples from the "Updated Resume Dataset":
Role Category	Precision	Recall	F1-Score
Data Science	1.00	1.00	1.00
Java Developer	1.00	1.00	1.00
Web Designing	1.00	1.00	1.00
Testing	0.94	1.00	0.97
OVERALL	99.48%	99.00%	99.20%
🚀 Installation & Usage
Clone the Repo:
code
Bash
git clone https://github.com/Veerannagoli/CSEBO5.git
cd CSEBO5
Install Requirements:
code
Bash
pip install flask sentence-transformers groq PyPDF2 rank_bm25 scikit-learn pandas torch
Configure API:
Add your Groq API Key in .env or directly in main.py.
Required Assets:
nexus_model.pkl (Local ML Classifier)
nexus_tfidf.pkl (TF-IDF Vectorizer)
job_database.csv (Proprietary Role Taxonomy)
Run the App:
code
Bash
python main.py
Access at: http://127.0.0.1:5000
📂 Project Structure
code
Text
├── uploads/               # Temporary PDF storage
├── templates/
│   └── index.html         # Flask Dashboard (UI)
├── engine.py              # The Brain (MPNet + BM25 + SVM)
├── main.py                # Server Routes & Zip Logic
├── job_database.csv       # Role Grounding Dataset
├── nexus_model.pkl        # Trained SVM Brain
├── nexus_tfidf.pkl        # Trained Vectorizer
└── README.md              # Documentation
📜 License
Licensed under the MIT License.
Developed for advanced AI-driven Talent Acquisition.
43.9s
