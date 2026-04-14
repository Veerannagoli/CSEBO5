NexHire AI | Next-Gen Talent Intelligence System








📌 Overview

NexHire AI is an advanced AI-powered recruitment engine designed to go beyond traditional keyword-based resume screening.

It leverages a Hybrid Inference Pipeline combining:

Machine Learning (SVM)
Information Retrieval (BM25)
Generative AI (Llama 3.1)

👉 Result: 99.48% accurate role classification + human-like reasoning insights

🧠 Technical Architecture — Tri-Layer Intelligence
1️⃣ Semantic Brain (Context Understanding)
Model: all-mpnet-base-v2 (Sentence Transformers)
Function: Converts resume & JD into 768-dimensional embeddings
Purpose: Captures meaning beyond keywords

✔ Example:
“ETL Pipelines” ≈ “Data Pipeline Development”

2️⃣ Lexical Engine (Precision Matching)
Algorithm: BM25 Okapi
Function: Scores keyword importance & rarity
Purpose: Ensures strict technical matching

✔ Example:
If JD requires Kubernetes, it must be present

3️⃣ Classification Layer (Local ML)
Model: LinearSVC (SVM) + TF-IDF
Dataset: 14,000+ resumes
Accuracy: 99.48% F1 Score

✔ Purpose:
Instant role prediction with zero API latency

4️⃣ Reasoning Layer (Explainable AI)
Model: Llama-3.1-8B (via Groq)
Function: Deep skill-gap analysis

✔ Provides:

Skill validation
Missing skills
Certification suggestions
🌟 Key Features

✔ Hybrid Scoring Formula

Final Score = [(Semantic × 0.7) + (Lexical × 0.3)] × 1.55

✔ Zero-Hallucination Grounding

Uses job_database.csv for verified roles

✔ Explainable AI (XAI)

Transparent decision-making

✔ Dynamic Weighting

Adjusts for Internship / Entry / Experienced

✔ Top-N Resume Export

Download ranked resumes as ZIP

✔ Intelligent Name Extraction

NLP-based extraction from PDFs
⚙️ Execution Flow
Resume Ingestion
Extract text using PyPDF2
Clean using Regex
Global Matching
Whole Resume vs Whole JD baseline
Role Classification
Predict category using SVM
Hybrid Scoring
Semantic (MPNet) + Lexical (BM25)
Score Calibration
Apply 1.55× boost
Real-Time Ranking
Display on Flask dashboard
Deep Analysis
Llama generates insights & gaps
📊 Model Performance
Role Category	Precision	Recall	F1-Score
Data Science	1.00	1.00	1.00
Java Developer	1.00	1.00	1.00
Testing	0.94	1.00	0.97
Network Security	1.00	1.00	1.00
Weighted Avg	99.48%	99.00%	99.20%
📂 Project Structure
├── uploads/               # Uploaded resumes
├── templates/
│   └── index.html         # UI Dashboard
├── engine.py              # Core ML + AI logic
├── main.py                # Flask backend
├── job_database.csv       # Role taxonomy
├── nexus_model.pkl        # Trained SVM model
├── nexus_tfidf.pkl        # TF-IDF vectorizer
└── README.md              # Documentation
🚀 Installation & Usage
1️⃣ Clone Repository
git clone https://github.com/Veerannagoli/CSEBO5.git
cd CSEBO5
2️⃣ Install Dependencies
pip install flask sentence-transformers groq PyPDF2 rank_bm25 scikit-learn pandas torch
3️⃣ Configure API Key
Add your Groq API key in main.py
4️⃣ Run the Application
python main.py
5️⃣ Open in Browser
http://127.0.0.1:5000
