from decouple import config
from config import DevelopmentConfig
from flask import Flask
from flask_bcrypt import Bcrypt
from flask_login import LoginManager 
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config.from_object(DevelopmentConfig)

login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_message_category = "danger"

# initialize the database object on the app
db = SQLAlchemy(app) 
migrate = Migrate(app, db) # ???
bcrypt = Bcrypt(app) # ???

# Registering Blueprints
from src.accounts.views import accounts_bp
from src.accounts.models import User
from src.core.views import core_bp

app.register_blueprint(accounts_bp)
app.register_blueprint(core_bp)

def load_user(user_id):
    return User.query.filter(User.id == int(user_id)).first()
