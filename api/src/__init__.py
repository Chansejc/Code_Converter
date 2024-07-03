import os, sys
import config
from flask_cors import CORS
from flask import Flask
from flask_bcrypt import Bcrypt
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config.from_object(config.DevelopmentConfig)
CORS(app)

# initialize the database object on the app
db = SQLAlchemy(app)
bcrypt = Bcrypt(app)

# Registering Blueprints
#from src.accounts.models import User
from src.accounts.views import accounts_bp
from src.core.views import core_bp

app.register_blueprint(accounts_bp)
app.register_blueprint(core_bp)

# You have to be in the REPL to Instantiate the DB in the Smorg dir
