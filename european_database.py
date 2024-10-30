
import sqlalchemy as db
engine = db.create_engine("sqlite:///european_database.sqlite")

conn = engine.connect() 

metadata = db.MetaData() 
division= db.Table('divisions', metadata, autoload_with=engine) 

query = division.select()
exe = conn.execute(query) 
result = exe.fetchmany(5) 
print(result)
