from flask import Flask, render_template, jsonify

app = Flask(__name__)

JOBS = [
  {
    'id': 1,
    'title': 'Data Analyst',
    'location': 'Bandung, Indonesia',
    'salary': 'Rp 50,000,000'
  },
  {
    'id': 2,
    'title': 'Data Scientist',
    'location': 'Sanggau, Indonesia',
    'salary': 'Rp 25,000,000'
  },
  {
    'id': 3,
    'title': 'Web Back-end Programmer',
    'location': 'Jakarta, Indonesia',
    'salary': 'Rp 100,000,000'
  },
  {
    'id': 4,
    'title': 'Web Front-end Programmer',
    'location': 'Remote',
    'salary': 'Rp 100,000,000'
  },
]

@app.route("/")
def hello():
  return render_template("home.html", jobs= JOBS,company_name = "Ganesa")

@app.route("/api/jobs")
def list_jobs():
  return jsonify(JOBS)

if __name__ == "__main__":
  app.run(host="0.0.0.0", debug=True)
