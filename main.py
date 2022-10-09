from flask import Flask, render_template, request, redirect
from extractors.wwr import extract_wwr_jobs
from extractors.remoteok import extract_remoteok_jobs

app = Flask("JobScrapper")

db = {}


@app.route("/")  # decorator - 바로 아래 있는 함수 실행
def home():
  return render_template("home.html")


@app.route("/search")
def search():
  keyword = request.args.get("keyword")
  if keyword == None:
    return redirect("/")
  if keyword in db:
    jobs = db[keyword]
  else:
    remoteok = extract_remoteok_jobs(keyword)
    wwr = extract_wwr_jobs(keyword)
    jobs = remoteok + wwr
    db[keyword] = jobs
  return render_template("search.html", keyword=keyword, jobs=jobs)


app.run("0.0.0.0")  # replit 에서 실행할 것이므로
