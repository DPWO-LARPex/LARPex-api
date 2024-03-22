from pathlib import Path
from dotenv import load_dotenv
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.sql import text
import os

load_dotenv()
SQLALCHEMY_DATABASE_URL = os.getenv("DATABASE_URL")

"""FOR SQLITE DATABASE"""
db_file_path = Path(SQLALCHEMY_DATABASE_URL).resolve()
engine = create_engine("sqlite:///example.db")

"""FOR OTHER DATABASES"""
# engine = create_engine(SQLALCHEMY_DATABASE_URL)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

"""PRE-PING DATABASE"""

try:
    db = SessionLocal()
    db.execute(text('SELECT 1'))
    db.close()
    print("DATABASE IS READY")
except Exception as e:
    print("DATABASE IS NOT READY")
    print(e)
    quit()
