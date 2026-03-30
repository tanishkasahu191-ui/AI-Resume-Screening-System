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