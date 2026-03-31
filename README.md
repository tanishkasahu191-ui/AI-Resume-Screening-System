
# AI Resume Screening System

## Problem
Recruiters receive many resumes and manually reviewing them takes a lot of time.

## Solution
This project automatically analyzes resumes and compares them with a job description using Natural Language Processing and cosine similarity.





## Usage
Upload a resume and paste a job description to calculate the similarity score.





## Overview

The **AI Resume Screening System** is a web-based application that helps automate the process of screening resumes. Recruiters often receive a large number of resumes for a single job position, making manual screening time-consuming.

This project uses **Natural Language Processing (NLP)** techniques to analyze resumes and compare them with a job description to calculate a **similarity score** that indicates how well a candidate matches the job requirements.

The system also extracts skills from the resume and identifies missing skills based on the job description.

---

## Features

* Upload resume in **PDF or DOCX format**
* Extract text from the uploaded resume
* Compare resume with a **job description**
* Calculate **AI-based similarity score**
* Extract **skills from the resume**
* Identify **missing skills**
* Provide **candidate rating and feedback**
* Web interface built using **Flask**

---

## Technologies Used

* Python
* Flask
* Natural Language Processing (NLP)
* TF-IDF Vectorization
* Cosine Similarity
* pdfplumber
* python-docx
* scikit-learn
* spaCy
* HTML & CSS
* GitHub for version control

---

## Project Structure

AI-Resume-Screening-System
app.py
resume_parser.py
similarity.py
requirements.txt
templates/index.html
templates/result.html
static/style.css
  README.md



```

### 2. Navigate to the project folder

```
cd AI-Resume-Screening-System
```

### 3. Install dependencies

```
pip install -r requirements.txt
```

### 4. Run the application

```
python app.py
```

### 5. Open in browser

Go to:

```
http://127.0.0.1:5000
```

---

## How to Use

1. Open the web application in your browser.
2. Upload a resume file (PDF or DOCX).
3. Enter a job description in the text box.
4. Click **Analyze Resume**.
5. The system will display:

   * Resume similarity score
   * Extracted skills
   * Missing skills
   * Candidate rating and feedback

---

## Example Workflow

Resume Upload → Text Extraction → NLP Processing → Similarity Calculation → Result Display




---
## Future Improvements
- Skill extraction
- Resume ranking
- Dashboard for recruiters
---

## Author

**Tanishka Sahu**
**25BCE10056**
B.Tech CSE Student

---

## GitHub Repository

https://github.com/tanishkasahu191-ui/AI-Resume-Screening-System

