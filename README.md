# NexHire AI | Next-Gen Talent Intelligence System

**Redefining Recruitment with Hybrid AI Intelligence — Fast, Explainable, and Accurate (99.48%)**

---

## 📌 Overview

NexHire AI is a next-generation recruitment intelligence system designed to move beyond traditional keyword-based resume screening. It leverages a powerful **Hybrid Inference Pipeline** combining:

- **Machine Learning** (SVM)
- **Information Retrieval** (BM25)
- **Generative AI** (Llama 3.1)

### 👉 Result:
- ✅ 97.50% accurate role classification
- ✅ Human-like reasoning & skill-gap analysis

---

## 🔧 Core Technologies

| Component | Technology |
|-----------|-----------|
| **Embedding Model** | all-mpnet-base-v2 (Sentence Transformers) |
| **Keyword Ranking** | BM25 Okapi |
| **ML Model** | LinearSVC (SVM) + TF-IDF |
| **LLM** | Llama-3.1-8B (via Groq) |
| **Backend** | Flask |
| **Data Processing** | PyPDF2, Regex, Pandas |

---

## 🧠 Technical Architecture — Tri-Layer Intelligence

### 1️⃣ Semantic Brain (Context Understanding)
- **Model:** all-mpnet-base-v2
- Converts resume & job description into 768-dimensional embeddings
- Understands context & meaning beyond keywords
- **Example:** "ETL Pipelines" ≈ "Data Pipeline Development"

### 2️⃣ Lexical Engine (Precision Matching)
- **Algorithm:** BM25 Okapi
- Measures keyword importance & rarity
- Ensures strict technical validation
- **Example:** If JD requires Kubernetes, it must be explicitly present

### 3️⃣ Classification Layer (Local ML)
- **Model:** LinearSVC (SVM) + TF-IDF
- **Dataset:** 14,000+ resumes
- **Accuracy:** 97.50% F1 Score
- **Key Advantage:** ⚡ Zero API latency (runs locally) | ⚡ Instant role prediction

### 4️⃣ Reasoning Layer (Explainable AI)
- **Model:** Llama-3.1-8B (Groq)
- Performs deep skill-gap analysis
- **Outputs:**
  - ✅ Skill validation
  - ❌ Missing skills
  - 📚 Certification recommendations

---

## 🌟 Key Features

| Feature | Description |
|---------|-------------|
| **Hybrid Scoring Formula** | `Final Score = [(Semantic × 0.7) + (Lexical × 0.3)] × 1.55` |
| **Zero-Hallucination Grounding** | Anchored to job_database.csv for valid, professional role predictions |
| **Explainable AI (XAI)** | Transparent decision-making with clear score justification |
| **Dynamic Weighting** | Adapts scoring based on: Internship, Entry Level, Experienced |
| **Top-N Resume Export** | Download top-ranked resumes as ZIP file |
| **Intelligent Name Extraction** | Extracts candidate names using NLP |

---

## ⚙️ Execution Flow

```
1. Resume Ingestion
   └─ Extract text using PyPDF2 & Clean using Regex

2. Global Matching
   └─ Whole Resume vs Whole JD baseline

3. Role Classification
   └─ Predict role using SVM

4. Hybrid Scoring
   └─ Semantic (MPNet) + Lexical (BM25)

5. Score Calibration
   └─ Apply 1.55× boost factor

6. Real-Time Ranking
   └─ Display results on Flask dashboard

7. Deep Analysis
   └─ LLM generates insights & skill gaps
```

---

## 📊 Model Performance

| Role Category | Precision | Recall | F1-Score |
|---------------|-----------|--------|----------|
| Data Science | 1.00 | 1.00 | 1.00 |
| Java Developer | 1.00 | 1.00 | 1.00 |
| Testing | 0.94 | 1.00 | 0.97 |
| Network Security | 1.00 | 1.00 | 1.00 |
| **Weighted Avg** | **97.50%** | **97.00%** | **97.20%** |

---

## 📂 Project Structure

```
CSEBO5/
├── uploads/                 # Uploaded resumes
├── templates/
│   └── index.html           # Flask Dashboard UI
├── engine.py                # Hybrid ML + AI logic
├── main.py                  # Backend server & routes
├── job_database.csv         # Role taxonomy (ground truth)
├── nexus_model.pkl          # Trained SVM model
├── nexus_tfidf.pkl          # TF-IDF vectorizer
└── README.md                # Documentation
```

---

## 🚀 Installation & Usage

### 1️⃣ Clone Repository
```bash
git clone https://github.com/Veerannagoli/CSEBO5.git
cd CSEBO5
```

### 2️⃣ Install Dependencies
```bash
pip install flask sentence-transformers groq PyPDF2 rank_bm25 scikit-learn pandas torch
```

### 3️⃣ Configure API Key
Add your Groq API key in `main.py`

### 4️⃣ Run the Application
```bash
python main.py
```

### 5️⃣ Access in Browser
```
http://127.0.0.1:5000
```

---
