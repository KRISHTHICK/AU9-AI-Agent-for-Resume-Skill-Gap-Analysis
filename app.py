import streamlit as st
import tempfile
from utils.extractor import extract_text_from_pdf, extract_text_from_docx
from agent.skill_agent import analyze_resume_vs_job

st.title("AI Resume Skill Gap Analysis Agent")

uploaded_resume = st.file_uploader("Upload your Resume (PDF/DOCX)", type=["pdf", "docx"])
job_description = st.text_area("Paste the Job Description")

if st.button("Analyze"):
    if uploaded_resume and job_description.strip():
        with tempfile.NamedTemporaryFile(delete=False) as tmp:
            tmp.write(uploaded_resume.read())
            tmp_path = tmp.name
        
        if uploaded_resume.name.endswith(".pdf"):
            resume_text = extract_text_from_pdf(tmp_path)
        else:
            resume_text = extract_text_from_docx(tmp_path)
        
        results = analyze_resume_vs_job(resume_text, job_description)
        
        st.subheader("✅ Skills in Resume")
        st.write(results["resume_skills"])
        
        st.subheader("📋 Skills in Job Description")
        st.write(results["job_skills"])
        
        st.subheader("🟢 Matched Skills")
        st.write(results["matched_skills"])
        
        st.subheader("🔴 Missing Skills")
        st.write(results["missing_skills"])
        
        st.subheader("📚 Learning Recommendations")
        st.write(results["recommendations"])
    else:
        st.warning("Please upload a resume and paste a job description.")
