from sqlalchemy import create_engine, text
import os

db_connection_string = os.environ['DB_CONNECTION_STRING']

engine = create_engine(db_connection_string)

def load_athletes_from_db():
    with engine.connect() as conn:
        result = conn.execute(text("select * from athletes"))
        athletes = []
        for row in result.all():
                athletes.append(row._asdict())
        return athletes      

