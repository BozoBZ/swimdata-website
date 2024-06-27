from sqlalchemy import create_engine, text
import urllib.parse

user_name = "avnadmin"
host="swimdata-mysql-swimdata.h.aivencloud.com:25477"
database = "swimdata_test1"
password = "AVNS_Nbl8nVYZdZTTu1AuXJj" 

encoded_password = urllib.parse.quote_plus(password)

connection_string = f"mysql+pymysql://{user_name}:{encoded_password}@{host}/{database}"
# Or, using engine configuration:
engine = create_engine(connection_string)

# engine=create_engine("mysql+pymysql://@swimdata-mysql-swimdata.h.aivencloud.com:25477/swimdata_test1")

def load_athletes_from_db():
    with engine.connect() as conn:
        result = conn.execute(text("select * from athletes"))
        athletes = []
        for row in result.all():
                athletes.append(row._asdict())
        return athletes      

