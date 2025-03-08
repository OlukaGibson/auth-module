import os
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

SQLALCHEMY_DATABASE_URL = 'postgresql://gibby:17wo8bQMeZ1SEMBd8KODSc8MPUjueGJR@dpg-cv66e97noe9s73brsg00-a.oregon-postgres.render.com/auth_tm5k' #os.getenv('DATABASE_URL') #'postgresql://postgres:Bright#1270@localhost/fastapi'

engine = create_engine(SQLALCHEMY_DATABASE_URL)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()