# AU9-AI-Agent-for-Resume-Skill-Gap-Analysis
Ai Agent

 AI Agent for Resume Skill Gap Analysis
Idea:
An AI agent that takes a user’s resume (PDF/DOCX) and compares it with a given job description, then produces a Skill Gap Report showing:

Skills the user already has

Missing skills required for the job

Suggested learning resources for missing skills

Features
File Upload – Upload your resume (PDF/DOCX) and paste the job description.

Skill Extraction – Extracts technical and soft skills from both resume and job description.

Skill Gap Analysis – Finds which skills are missing.

Learning Recommendations – Suggests online resources to learn the missing skills.

Tech Stack
Streamlit – Web UI

PyMuPDF / docx2txt – Extract text from PDF/DOCX

spaCy – NLP-based skill extraction

OpenAI / Ollama (local) – Generate recommendations

Python – Backend logic

pip install -r requirements.txt
python -m spacy download en_core_web_sm

How It Works
User uploads resume (PDF/DOCX) and pastes job description.

Text extraction happens using PyMuPDF (.pdf) or docx2txt (.docx).

Skill extraction uses a predefined list + NLP matching.

Comparison finds missing and matched skills.

AI Agent generates learning suggestions using OpenAI or fallback static tips.

Streamlit UI displays the full analysis.
