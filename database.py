from sqlalchemy import create_engine, text
import os

# online database data
databaseName = os.environ['DATABASENAME']
username = os.environ['DATABASE_USER_NAME']
host = os.environ['DATABASE_HOST']
password = os.environ['DATABASE_PASSWORD']

url = f"mysql+pymysql://{username}:{password}@{host}/{databaseName}"

engine = create_engine(
  url,
  connect_args={
    "ssl": {
      "sca": "/etc/ssl/cert.pem"

      # or this works as well
      # "ssl_ca": "/etc/ssl/cert.pem"

      # this doesn't work, though ca is mentioned in documentation
      # "ca": "/etc/ssl/cert.pem"
    }
  })


def load_jobs_from_db():
  with engine.connect() as conn:
    result = conn.execute(text('select * from jobs'))

    # res_all=result.all()
    # res_keys=result.keys()
    # # print(dir(result))
    # res_dict=zip(res_keys,res_all[0])
    # print(dict(res_dict))
    # # print(res_all)

    res_keys = result.keys()
    jobs = []
    for row in result.all():
      temp = dict(zip(res_keys, row))
      jobs.append(temp)

    return jobs


def load_job_from_db(id):
  with engine.connect() as conn:
    # result = conn.execute(text('select * from jobs where job_id=:val'),val=id)

    result = conn.execute(text(f'select * from jobs where job_id={id}'))
    res_keys = result.keys()
    rows = result.all()
    if len(rows) == 0:
      return None
    else:
      return dict(zip(res_keys, rows[0]))


# created application table using mysql-workbench. Here we're just adding data to it.
def add_application_data_to_db(job_id, data):
  with engine.connect() as conn:
    query = text(
      "insert into application (job_id, full_name, email, linkedinUrl, education,work_experience,resumeUrl) values (:job_id, :full_name,:email, :linkedin, :education, :workExp,:resume_url)"
    )

    conn.execute(
      query, {
        'job_id': job_id,
        'full_name': data['full_name'],
        'email': data['email'],
        'linkedin': data['linkedin'],
        'education': data['education'],
        'workExp': data['workExp'],
        'resume_url': data['resume_url']
      })
