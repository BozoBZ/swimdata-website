from sqlalchemy import create_engine, text

engine=create_engine("mysql+pymysql://avnadmin:AVNS_Nbl8nVYZdZTTu1AuXJj@swimdata-mysql-swimdata.h.aivencloud.com:25477/swimdata_test1")

def load_athletes_from_db():
    with engine.connect() as conn:
        result = conn.execute(text("select * from athletes"))
        athletes = []
        for row in result.all():
                athletes.append(row._asdict())
        return athletes      

