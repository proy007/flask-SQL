from flask import Flask, render_template, jsonify
from database import load_jobs_from_db, load_job_from_db

app = Flask(__name__)

# JOBS = [
#   {
#     'id': 11111,
#     'title': 'Web Devloper',
#     'location': 'Bangalore, Karnataka',
#     'salary': 'Rs 20,000'
#   },
#   {
#     'id': 22222,
#     'title': 'Cook',
#     'location': 'Mumbai, Maharastra',
#     'salary': 'Rs 20,000'
#   },
#   {
#     'id': 33333,
#     'title': 'Teacher',
#     'location': 'Siliguri, West Bengal',
#     'salary': 'Rs 20,000'
#   },
#   {
#     'id': 44444,
#     'title': 'Researcher',
#     'location': 'Gurgaon, Haryana',
#     'salary': 'Rs 20,000'
#   },
#   {
#     'id': 55555,
#     'title': 'Data Analytics',
#     'location': 'Surat, Gujarat'
#   },
#   {
#     'id': 66666,
#     'title': 'Data Scientist',
#     'location': 'Austin, Texas'
#   },
# ]

# imported from database.py
jobs = load_jobs_from_db()


@app.route("/")
def hello_world():
  return render_template('home.html', jobs=jobs, company_name='Practo')


@app.route("/api/job")
def list_jobs_api():
  return jsonify(jobs)


@app.route("/job/<id>")
def show_jobs(id):
  job = load_job_from_db(id)
  if not job:
    return '<h1>404:Not Found'
  else:
    return render_template('jobpage.html', job=job)


if __name__ == '__main__':
  app.run(host='0.0.0.0', debug=True)
