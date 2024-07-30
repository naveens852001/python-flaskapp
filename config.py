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
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://postgres:postgres@localhost/clouddb'
    SECRET_KEY = 'developmentKey'

    # def __init__(self):
    #     db=SQLAlchemy()
