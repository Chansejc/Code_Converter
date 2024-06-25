from datetime import datetime
from src import bcrypt, db

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
        return  \
        f"""
        <Email: {self.email}>
        <ID: {self.id}>
        <Date Created: {self.created_on}>
        <Awaiting Removal: {self.awaiting_removal}>
        """
