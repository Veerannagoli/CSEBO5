import os
import zipfile
from io import BytesIO
from flask import Flask, render_template, request, jsonify, send_file
from werkzeug.utils import secure_filename
from engine import ResumeRankingEngine
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)
UPLOAD_FOLDER = 'uploads'
os.makedirs(UPLOAD_FOLDER, exist_ok=True)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

# Initialize Engine
GROQ_API_KEY = os.getenv("GROQ_API_KEY")
engine = ResumeRankingEngine(GROQ_API_KEY)

# Global variable to store last results for downloading (for simplicity in this project)
last_ranked_results = []

@app.route("/", methods=["GET", "POST"])
def index():
    global last_ranked_results
    jd, level, results = "", "entry", []

    if request.method == "POST":
        jd = request.form.get("jd")
        level = request.form.get("level")
        files = request.files.getlist("resumes")
        
        if files and jd:
            file_paths = []
            for f in files:
                if f.filename:
                    filename = secure_filename(f.filename)
                    path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
                    f.save(path)
                    file_paths.append(path)

            results = engine.rank_resumes(file_paths, jd, level)
            last_ranked_results = results # Save for download route

    return render_template("index.html", results=results, jd=jd, level=level)

@app.route("/download_top", methods=["POST"])
def download_top():
    global last_ranked_results
    if not last_ranked_results:
        return "No results to download", 400

    # Get number of resumes to download from form
    try:
        n = int(request.form.get("top_n", 3))
    except:
        n = 3

    # Take the top N results
    top_resumes = last_ranked_results[:n]

    # Create ZIP in memory
    memory_file = BytesIO()
    with zipfile.ZipFile(memory_file, 'w') as zf:
        for res in top_resumes:
            filename = res['filename']
            file_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
            if os.path.exists(file_path):
                zf.write(file_path, filename)
    
    memory_file.seek(0)
    return send_file(memory_file, download_name=f"top_{n}_resumes.zip", as_attachment=True)

@app.route("/get_report")
def get_report():
    filename = request.args.get("filename")
    jd = request.args.get("jd")
    path = os.path.join(app.config['UPLOAD_FOLDER'], secure_filename(filename))
    if os.path.exists(path):
        report = engine.generate_deep_report(path, jd)
        return jsonify(report)
    return jsonify({"error": "File not found"}), 404

if __name__ == "__main__":
    app.run(debug=True)