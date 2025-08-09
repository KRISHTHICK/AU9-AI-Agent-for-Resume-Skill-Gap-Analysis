from utils.skill_utils import extract_skills, compare_skills
import openai
import os

openai.api_key = os.getenv("OPENAI_API_KEY")  # or use Ollama

def analyze_resume_vs_job(resume_text, job_text):
    resume_skills = extract_skills(resume_text)
    job_skills = extract_skills(job_text)
    
    matched, missing = compare_skills(resume_skills, job_skills)
    
    recommendations = generate_learning_recommendations(missing)
    
    return {
        "resume_skills": resume_skills,
        "job_skills": job_skills,
        "matched_skills": matched,
        "missing_skills": missing,
        "recommendations": recommendations
    }

def generate_learning_recommendations(missing_skills):
    if not missing_skills:
        return ["No missing skills. You're job ready!"]
    
    prompt = f"Suggest online learning resources for these skills: {', '.join(missing_skills)}"
    
    try:
        response = openai.Completion.create(
            model="text-davinci-003",
            prompt=prompt,
            max_tokens=150
        )
        return response.choices[0].text.strip().split("\n")
    except Exception:
        return [f"Search on Google or YouTube for '{skill} tutorials'" for skill in missing_skills]
