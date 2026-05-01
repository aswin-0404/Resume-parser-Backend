import re

COMMON_SKILLS = [
    "python", "django", "react", "javascript",
    "sql", "postgresql", "html", "css",
    "java", "c++", "node", "express"
]

def parse_resume_simple(text):
    text_lower = text.lower()

    email = re.findall(r'\S+@\S+', text)
    email = email[0] if email else ""

    phone = re.findall(r'\d{10}', text)
    phone = phone[0] if phone else ""

    skills = [skill for skill in COMMON_SKILLS if skill in text_lower]

    name = text.split("\n")[0] if text else ""

    exp_match = re.findall(r'(\d+)\+?\s+years', text_lower)
    experience = int(exp_match[0]) if exp_match else 0

    return {
        "name": name.strip(),
        "email": email,
        "phone": phone,
        "skills": skills,
        "experience": experience,
        "education": "",
        "current_company": ""
    }
