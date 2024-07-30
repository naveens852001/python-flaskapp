
from app import app , db  # Import your app and db from your main application file
from models import Cloud  # Import your models

with app.app_context():
    db.create_all()
    print("Database initialized!")