import pdfplumber
from docx import Document

def extract_text(file_path):
    text=""

    if file_path.endswith(".pdf"):
        with pdfplumber.open(file_path) as pdf:
            for page in pdf.pages:
                text+=page.extract_text() or ""
    elif file_path.endswith(".docx"):
        doc=Document(file_path)
        text="\n".join([para.text for para in doc.paragraphs])
    
    return text

def match_candidate_job(candidate,job):
    candidate_skills=set([s.lower() for s in candidate.skills])
    job_skills = set([s.lower() for s in job.skills])

    matched = candidate_skills & job_skills

    skill_score= (len(matched) / len(job_skills)) * 100 if job_skills else 0

    if candidate.experience >= job.experience:
        exp_score=100
        exp_gap=0
    else:
        exp_score=50
        exp_gap=job.experience - candidate.experience

    final_score=(0.7 * skill_score) + (0.3 * exp_score)

    return {
        "score": round(final_score, 2),
        "matched_skills": list(matched),
        "missing_skills": list(job_skills - matched),
        "experience_gap": exp_gap
    }