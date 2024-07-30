import os


# db = None

# def get_db():
#     if db:
#         return db
#     return SQLAlchemy()

class Config:
    db_username = "postgres"
    db_password = "postgres"
    db_hostname = "localhost"
    db_name = "clouddb"
  
    # 'postgresql+psycopg2://<username>:<password>@<hostname>/<dbname>'
    SQLALCHEMY_DATABASE_URI = 'postgresql://postgres.hngcwvhamxnjrhjfpywo:naveensharmadatabase@aws-0-ap-south-1.pooler.supabase.com:6543/postgres'
    
    SECRET_KEY = 'developmentKey'
    # SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://postgres:postgres@localhost/clouddb'
 
    
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    # def __init__(self):
    #     db=SQLAlchemy()
