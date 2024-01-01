from sqlalchemy import create_engine, text
import os

db_connector = os.environ['DB_CONNECTOR']

engine = create_engine(
  db_connector,
    connect_args={
        "ssl": {
            "ssl_ca": "/etc/ssl/cert.pem",
        }
    }
)

def load_jobs_db():
  with engine.connect() as conn:
    result = conn.execute(text("SELECT * FROM jobs"))

    jobs = []
    for row in result.all():
      jobs.append(row._mapping)
    return jobs