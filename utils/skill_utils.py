import spacy
nlp = spacy.load("en_core_web_sm")

COMMON_SKILLS = [
    "Python", "Java", "C++", "SQL", "Machine Learning", "Deep Learning",
    "Data Analysis", "Project Management", "Communication", "Leadership",
    "AWS", "Azure", "Docker", "Kubernetes", "React", "Node.js", "Excel"
]

def extract_skills(text):
    doc = nlp(text)
    found_skills = set()
    for skill in COMMON_SKILLS:
        if skill.lower() in text.lower():
            found_skills.add(skill)
    return list(found_skills)

def compare_skills(resume_skills, job_skills):
    missing = list(set(job_skills) - set(resume_skills))
    matched = list(set(resume_skills) & set(job_skills))
    return matched, missing
