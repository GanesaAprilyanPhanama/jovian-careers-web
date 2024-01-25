from flask import Flask, render_template, jsonify

app = Flask(__name__)

JOBS = [
  {
    'id': 1,
    'title': 'Underwater Dweller',
    'location': 'Bandung, Indonesia',
    'salary': 'Rp 50,000,000'
  },
  {
    'id': 2,
    'title': 'Cargo Ship Sailor',
    'location': 'Sanggau, Indonesia',
    'salary': 'Rp 25,000,000'
  },
  {
    'id': 3,
    'title': 'Somali Pirate',
    'location': 'Jakarta, Indonesia',
    'salary': 'Rp 100,000,000'
  },
  {
    'id': 4,
    'title': 'Slave',
    'location': 'Remote',
    'salary': 'Rp 100,000,000'
  },
]

@app.route("/")
def hello():
  return render_template("home.html", jobs= JOBS,company_name = "Sail'em")

@app.route("/api/jobs")
def list_jobs():
  return jsonify(JOBS)

if __name__ == "__main__":
  app.run(host="0.0.0.0", debug=True)
