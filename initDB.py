from main import db, Book, app

db.create_all(app=app)

print("Database Initialzed")