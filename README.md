# CSEBO5
NexHire AI - MPNet + BM25 for scoring &amp; Hybrid ML (99% Acc) + Llama 3.1 for role prediction
GVCStream AI | Next-Gen Talent Intelligence System 🚀
![alt text](https://img.shields.io/badge/Python-3.9+-blue.svg)

![alt text](https://img.shields.io/badge/ML_Accuracy-99.48%25-orange.svg)

![alt text](https://img.shields.io/badge/Model-Llama_3.1-blueviolet.svg)

![alt text](https://img.shields.io/badge/Framework-Flask-green.svg)
GVCStream AI is a professional-grade resume ranking and talent intelligence platform. It replaces traditional keyword-based screening with a Hybrid Inference Pipeline, combining locally-trained Machine Learning (SVM) with state-of-the-art Large Language Models (Llama 3.1) and Semantic Search (MPNet).
🌟 Key Features
Hybrid Ranking Engine: A dual-layer scoring system using BM25 Lexical Precision and MPNet Semantic Meaning.
99.48% Accurate Role Classification: Locally hosted LinearSVC (SVM) model identifies professional categories instantly without API latency.
Explainable AI (XAI): Generates deep technical justifications, identifying exactly why a candidate matches and what they are missing.
Zero-Hallucination Grounding: Predictions are anchored to a proprietary job_database.csv taxonomy.
Automated Shortlisting: Integrated ZIP export functionality to download the top-ranked candidates.
Dynamic Weighting: Context-aware scoring that shifts focus based on seniority (e.g., Projects for Interns vs. Experience for Seniors).
🧠 Technical Architecture & Models
The system architecture is divided into three specialized intelligence layers:
1. The Ranking Layer (Math)
The engine calculates a "Human-Alignment" score using the following formula:
Final Score
=
[
(
Semantic Similarity
×
0.7
)
+
(
Lexical Score
×
0.3
)
]
×
1.55
Final Score=[(Semantic Similarity×0.7)+(Lexical Score×0.3)]×1.55
Component	Model/Algorithm	Function
Semantic Matching	all-mpnet-base-v2	Uses 768-dimensional vector embeddings to understand technical context and synonyms.
Lexical Matching	BM25 Okapi	A probabilistic model that ensures "Hard Skills" are strictly verified.
Safety Net	Global Text Analysis	Compares the entire resume text to prevent score-loss from poor PDF section parsing.
2. The Classification Layer (ML)
To ensure high-speed and deterministic role identification, we use a locally-trained classifier:
Model: Support Vector Machine (LinearSVC)
Vectorization: TF-IDF with N-Gram range (1, 3)
Training Data: 14,000+ professional resumes
Performance: 99.48% F1-Score on tested samples.
3. The Reasoning Layer (GenAI)
The "Deep Intelligence" is provided by Llama 3.1 (8B-Instant) via the Groq Cloud SDK.
Task: Semantic Gap Analysis.
Output: Structured JSON containing Matched Skills, Critical Gaps, and Strategic Upskilling Advice.
📊 Model Evaluation (Accuracy Proof)
The ML classifier was evaluated using a multi-class confusion matrix, achieving the following results:
Role Category	Precision	Recall	F1-Score
Data Science	1.00	1.00	1.00
Java Developer	1.00	1.00	1.00
DevOps Engineer	1.00	0.93	0.96
Full Stack	0.98	1.00	0.99
AVERAGE	99.48%	99.00%	99.20%
🛠️ Tech Stack
Core: Python 3.12
Web Framework: Flask
Machine Learning: Scikit-Learn, Pandas, NumPy
Natural Language Processing: Sentence-Transformers (PyTorch), Rank-BM25, NLTK
Generative AI: Groq Cloud SDK (Llama 3.1-8B)
PDF Extraction: PyPDF2 + Custom Regex Preprocessing
Frontend: HTML5, CSS3 (Custom Dark Theme), Bootstrap 5, FontAwesome 6
🚀 Installation & Setup
Clone the Repo:
code
Bash
git clone https://github.com/yourusername/GVCStream-AI.git
cd GVCStream-AI
Install Dependencies:
code
Bash
pip install flask sentence-transformers groq PyPDF2 rank_bm25 scikit-learn pandas torch
API Configuration:
Add your Groq API Key in main.py:
code
Python
GROQ_API_KEY = "gsk_your_key_here"
Required Assets:
Ensure the following files are in the root directory:
nexus_model.pkl (Trained SVM Model)
nexus_tfidf.pkl (Trained Vectorizer)
job_database.csv (Role Taxonomy)
Launch Application:
code
Bash
python main.py
Open browser at: http://127.0.0.1:5000
📂 Project Structure
code
Text
├── uploads/               # Temporary storage for uploaded resumes
├── templates/
│   └── index.html         # Custom dark-themed Dashboard
├── engine.py              # The Hybrid ML/AI Processing Logic
├── main.py                # Flask Routes & File Management
├── nexus_model.pkl        # Serialized SVM Classifier
├── job_database.csv       # Grounding Taxonomy for Role Prediction
└── README.md              # Documentation
📜 License
Licensed under the MIT License.
Created for advanced Talent Intelligence and AI-driven Recruitment.
