from sqlalchemy import create_engine, MetaData

DATABASE_URL = "mysql+mysqlconnector://root:rajesh@localhost:3306/upi_db"

engine = create_engine(DATABASE_URL)
meta = MetaData()
conn = engine.connect()