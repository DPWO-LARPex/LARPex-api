from pathlib import Path
from dotenv import load_dotenv
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.sql import text
from models.base_gen import Base
from config.preinit_db import init_db_data
import os

load_dotenv()
SQLALCHEMY_DATABASE_URL = os.getenv("DATABASE_URL")
USE_SQLITE_DB = os.getenv("USE_SQLITE_DB") == "True"

print(USE_SQLITE_DB)

"""FOR SQLITE DATABASE"""
if(USE_SQLITE_DB):
    engine = create_engine("sqlite:///example.db")

"""FOR OTHER DATABASES"""
if(not USE_SQLITE_DB):
    engine = create_engine(SQLALCHEMY_DATABASE_URL)

"""CREATE TABLES"""
def create_tables():
    Base.metadata.create_all(bind=engine)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

"""DEPENDENCY"""
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


"""PRE-PING DATABASE"""

try:
    db = SessionLocal()
    if(USE_SQLITE_DB):
        create_tables() # TODO: REMOVE THIS LINE IN PRODUCTION
    #init_db_data(db) # TODO: REMOVE THIS LINE IN PRODUCTION
    db.execute(text('SELECT 1'))
    db.close()
    print("DATABASE IS READY")
    if(USE_SQLITE_DB):
        print("DB DEBUG")
    else:
        print("DB PRODUCTION")
except Exception as e:
    print("DATABASE IS NOT READY")
    print(e)
    quit()
