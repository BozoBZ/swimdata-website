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

def load_times_from_db():
    with engine.connect() as conn:
        result = conn.execute(text("select * from times"))
        times = []
        for row in result.all():
                times.append(row._asdict())
        return times      

def load_athlete_from_db(idAthlete):
    with engine.connect() as conn:
        result = conn.execute(text("select * from                                             athletes where idAthlete = :id"), {"id":                               idAthlete})
        rows = result.all()
        if len(rows)==0:
            return None
        else:
            return rows[0]._asdict()

def add_time_into_db(idAthlete, data):
    with engine.connect() as conn:
        query = text("INSERT INTO times (swimevent, idAthlete,                            idMeet,swimtime, swimtype) VALUES                                   (:swimevent, :idAthlete, :idMeet, :swimtime,                        :swimtype)")
        
        conn.execute(query, 
                     {
                        "swimevent" :data['swimevent'],
                        "idAthlete" :idAthlete,
                        "idMeet" :data['meet'],
                        "swimtime" :data['swimtime'],                                      "swimtype" :data['swimtype']
                     })  
        
        conn.commit()
