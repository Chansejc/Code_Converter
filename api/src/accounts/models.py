from datetime import datetime
from src import bcrypt, db

def get_user(email, model):
    user = list(filter(lambda x: x.email == email, db.session.query(model).all()))
    print("Here!")
    if user == []: raise UserNotFound("User Not Found")
    print("There!")
    print("User =>", user)
    return user[0] 

class UserNotFound(Exception):
    pass

class User(db.Model):
    __tablename__ = "users"

    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(100), unique=True, nullable=False)
    password = db.Column(db.String, nullable=False)
    created_on = db.Column(db.DateTime, nullable=False)
    awaiting_removal = db.Column(db.Boolean, nullable=False)

    def __init__(self, email, password):
        self.email = email
        self.password = bcrypt.generate_password_hash(password)
        self.created_on = datetime.now()
        self.awaiting_removal = False

    def __repr__(self):
        return f"'Email': {self.email}, 'ID': {self.id}, 'Date Created': {self.created_on}, 'Awaiting Removal': {self.awaiting_removal}" 

class Entry(db.Model):
    __tablename__ = "user_entries"

    entry_id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, nullable=False)
    file_id = db.Column(db.String, nullable=False, unique=True)
    created_on = db.Column(db.DateTime, nullable=False)

    def __init__(self, user_id: int, file_id: str):
        self.user_id = user_id
        self.file_id = file_id
        self.created_on = datetime.now()

    def __repr__(self):
        return f"<|File: {self.file_id}|User:{self.user_id}|>"

