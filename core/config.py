import os
from sqlalchemy import create_engine, MetaData
from sqlalchemy.orm import sessionmaker

# from password_manager import BASE_DIR

# get current directory
path = os.getcwd()
# print("Current Directory", path)
    
# prints parent directory
# print(os.path.abspath(os.path.join(path, os.pardir)))
BASE_DIR = os.path.abspath(os.path.join(path, os.pardir)) 

connection_str = "sqlite:///"+os.path.join(BASE_DIR, 'password_manager', 'manager.db')

# Database Engine
engine = create_engine(connection_str, echo=False, future=True)
connection = engine.connect()

# MetaData
meta = MetaData(bind=engine)

# For Database Transactions 
session = sessionmaker()

# print(BASE_DIR)
# print(connection_str)
