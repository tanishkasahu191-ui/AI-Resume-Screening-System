import docx
import pdfplumber
import spacy
# Error occurs if this isn't exactly right
nlp = spacy.load("en_core_web_sm")

def extract_text(file):

    text = ""

    if file.filename.endswith(".pdf"):
        with pdfplumber.open(file) as pdf:
            for page in pdf.pages:
                text += page.extract_text()

    elif file.filename.endswith(".docx"):
        doc = docx.Document(file)
        for para in doc.paragraphs:
            text += para.text

    return text


skills_list = [
"python","java","c++","sql","machine learning",
"flask","django","html","css","javascript",
"react","node","data analysis","deep learning"
]


def extract_skills(text):

    text = text.lower()
    found_skills = []

    for skill in skills_list:
        if skill in text:
            found_skills.append(skill)

    return found_skills


def missing_skills(resume_text, job_desc):

    resume_words = set(resume_text.lower().split())
    job_words = set(job_desc.lower().split())

    missing = job_words - resume_words

    return list(missing)[:10]