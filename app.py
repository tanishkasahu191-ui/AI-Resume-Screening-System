from flask import Flask, render_template, request
from resume_parser import extract_text
from similarity import get_similarity

app = Flask(__name__)

@app.route("/", methods=["GET","POST"])
def index():

    if request.method == "POST":

        resume = request.files["resume"]
        job_desc = request.form["jobdesc"]

        resume_text = extract_text(resume)

        score = get_similarity(resume_text, job_desc)

        return render_template("result.html", score=score)

    return render_template("index.html")


if __name__ == "__main__":
    app.run(debug=True)