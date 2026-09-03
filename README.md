# OmniTask AI: Agentic Document & Workflow Optimizer

An intelligent, multi-agent workflow automation application built for the Razorpay AI Buildathon. OmniTask AI takes unstructured project guidelines, academic syllabi, or complex PDFs and instantly transforms them into structured, actionable milestone execution databases.

## 🏗️ System Architecture

```text
[User Interface] (.pdf/.txt Dropzone)
       │
       ▼ (POST Multipart Stream)
[Flask Backend Server] (Port 8000)
       │
       ▼ (PyPDF Stream Extraction)
[Text Extraction Layer] (Raw Text Aggregation)
       │
       ▼ (Structured Schema Injection)
[Google Gemini AI Core] (JSON Constraint Framework)
       │
       ▼ (Strict Response Validation)
[Live Operational Action Board] (Dynamic Dashboard UI counters)
```

## 🛠️ Technical Stack & Frameworks
* **Runtime Core:** Python 3.x
* **Server Middleware:** Flask Engine (Pure-Python Context Runtime)
* **Ingestion Layer:** PyPDF Extraction Module
* **Interface Matrix:** HTML5, Modern CSS3, responsive Bootstrap 5 grid layout

## 🚀 Local Deployment Setup
1. Clone the repository: `git clone https://github.com/emmadivashishta-cpu/omnitask-ai.git`
2. Run installation: `pip install Flask Flask-CORS requests pypdf python-dotenv`
3. Spin up the server engine: `python app.py`
