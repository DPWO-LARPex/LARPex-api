from pathlib import Path
from dotenv import load_dotenv
from sqlalchemy import create_engine
from sshtunnel import SSHTunnelForwarder
from sqlalchemy.orm import sessionmaker
from sqlalchemy.sql import text
from config.config import build_db_url
from models.base_gen import Base
from config.preinit_db import init_db_data
from urllib.parse import urlparse, urlunparse
import os
import paramiko

load_dotenv()
SQLALCHEMY_DATABASE_URL = os.getenv("DATABASE_URL")
USE_SQLITE_DB = os.getenv("USE_SQLITE_DB") == "True"
SSH_HOST = os.getenv("SSH_HOST")
SSH_PORT = int(os.getenv("SSH_PORT"))
SSH_USER = os.getenv("SSH_USER")
SSH_KEY_PATH = os.getenv("SSH_KEY_PATH")

DB_HOST = os.getenv("DB_HOST")
DB_USER = os.getenv("DB_USER")
DB_PASSWORD = os.getenv("DB_PASSWORD")
DB_NAME = os.getenv("DB_NAME")
DB_PORT = int(os.getenv("DB_PORT"))
DB_DRIVER = os.getenv("DB_DRIVER")
SSH_KEY = paramiko.Ed25519Key.from_private_key_file(filename=SSH_KEY_PATH)

"""FOR SQLITE DATABASE"""
if(USE_SQLITE_DB):
    engine = create_engine("sqlite:///example.db")

"""FOR OTHER DATABASES"""
if(not USE_SQLITE_DB):
    server = SSHTunnelForwarder(
        (SSH_HOST, SSH_PORT),
        ssh_username=SSH_USER,
        ssh_pkey=SSH_KEY,
        remote_bind_address=(DB_HOST, DB_PORT) 
        )
    server.start()
    server.check_tunnels()
    print("SSH TUNNEL IS UP")
    print(server.tunnel_is_up, flush=True)
    local_port = str(server.local_bind_port)
    db_url = build_db_url(
        DB_DRIVER,
        DB_USER,
        DB_PASSWORD,
        "localhost",
        local_port,
        DB_NAME
    )
    #engine = create_engine(SQLALCHEMY_DATABASE_URL)
    engine = create_engine(db_url)

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
