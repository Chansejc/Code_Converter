from datetime import datetime
from flask_login import UserMixin 
# UserMixin 
#   ^- Adds mandatory properties and methods for a User class in authentication.
#   is_authenticated | is_active | is_anonymous | get_id()

from src import bcrypt, db

class User(UserMixin, db.Model):
    __tablename__ = "users"

    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(100), unique=True, nullable=False)
    password = db.Column(db.String, nullable=False)
    created_on = db.Column(db.DateTime, nullable=False)
    is_admin = db.Column(db.Boolean, nullable=False, default=False)

    def __init__(self, email, password, is_admin=False):
        self.email = email
        self.password = bcrypt.generate_password_hash(password)
        self.created_on = datetime.now()
        self.is_admin = is_admin

    def __repr__(self):
        return  \
        f"""
        <Email: {self.email}>
        <ID: {self.id}>
        <Date Created: {self.created_on}>
        <Is Admin?: {self.email}>
        """

