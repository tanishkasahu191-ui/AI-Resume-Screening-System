from flask import Flask, render_template, request
from resume_parser import extract_text, extract_skills, missing_skills
from similarity import get_similarity

app = Flask(__name__)

@app.route("/", methods=["GET","POST"])
def index():

    if request.method == "POST":

        resume = request.files["resume"]
        job_desc = request.form["jobdesc"]

        resume_text = extract_text(resume)

        score = get_similarity(resume_text, job_desc)

        skills = extract_skills(resume_text)

        missing = missing_skills(resume_text, job_desc)

        if score < 40:
            feedback = "Weak match. Improve your resume."
        elif score < 70:
            feedback = "Moderate match. Some improvements needed."
        else:
            feedback = "Strong match for this job."

        return render_template(
            "result.html",
            score=score,
            skills=skills,
            missing=missing,
            feedback=feedback
        )

    return render_template("index.html")


if __name__ == "__main__":
    app.run(debug=True)