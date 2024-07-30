from flask import Flask
from config import Config
from flask_sqlalchemy import SQLAlchemy


app = Flask("customer_app")
app.config.from_object(Config)
db = SQLAlchemy(app)

# To fix :ImportError: cannot import name 'db' from partially initialized module 'app' (most likely due to a circular import)
# Import models at the end to avoid circular import issues
from models import *
import views
import urls

if __name__ == '__main__':
    app.run(debug=True)
