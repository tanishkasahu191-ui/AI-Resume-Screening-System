import PyPDF2
import docx

def extract_text(file):

    text = ""

    if file.filename.endswith(".pdf"):
        reader = PyPDF2.PdfReader(file)

        for page in reader.pages:
            text += page.extract_text()

    elif file.filename.endswith(".docx"):
        doc = docx.Document(file)

        for para in doc.paragraphs:
            text += para.text

    return text
skills_list = [
"python","java","c++","sql","machine learning",
"flask","django","html","css","javascript"
]

def extract_skills(text):
    text = text.lower()
    found = []

    for skill in skills_list:
        if skill in text:
            found.append(skill)

    return found