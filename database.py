# import sqlalchemy
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


def load_job_from_db():
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


load_job_from_db()
