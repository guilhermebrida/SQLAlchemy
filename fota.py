import sqlalchemy as db

user = "postgres"
password = "postgres"
host = "localhost"
port = "54320"  
database = "fota"


url = f"postgresql://{user}:{password}@{host}:{port}/{database}"


engine = db.create_engine(url)

conn = engine.connect() 

metadata = db.MetaData()

devices= db.Table('devices', metadata, autoload_with=engine)

query = devices.select()

exe = conn.execute(query) 
result = exe.fetchmany(5) 
print(result)


























