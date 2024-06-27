from flask import Blueprint, jsonify
from sqlalchemy import delete
from src.accounts import models
from src import db
from src import bcrypt
import flask

# Blueprint todos:
## Setup email verification for account creation and account removal. (SMTP email Library)

accounts_bp = Blueprint("accounts", __name__)

@accounts_bp.route("/api/accounts/email_available/<email>/", methods=["GET"])
def test(email):
    if '@' not in email: return flask.Response("Insufficient Query URL", 401)
    users = list(filter(lambda x: x.email == email, db.session.query(models.User).all()))
    if users: return jsonify({"Status": "Fail"}) 
    return jsonify({"Status": "Success"}) 

@accounts_bp.route("/api/accounts/create/<email>/<pw>", methods=["POST"])
def new(email, pw):
    print(f"<Attempting to add User( Email: {email} )")
    try:
        db.session.add(models.User(email=email, password=pw))
        db.session.commit()
        print(f"<Successfuly added User( Email: {email} )")
        return jsonify({"Status": "Success"})
    except Exception as e:
        print("Problem at endpoint [ACCOUNTS >> CREATE]",e)
        return jsonify({"Status": "Fail"})

@accounts_bp.route("/api/accounts/verify_removal/<email>/", methods=["GET"])
def verify_removal():
    return flask.Response(str(True),200)

@accounts_bp.route("/api/accounts/remove/<email>/", methods=["POST"])
# This route must only be possible if the removal has been verified through the users email.
def remove(email):
    user_id = list(filter(lambda x: x.email == email, db.session.query(models.User).all()))[0].id
    user = db.session.get(models.User, user_id) 
    if user:
        if user.awaiting_removal:
            db.session.delete(user)
            db.session.commit()
            return jsonify({"Status": "Success"})
        return jsonify({"Status": "Fail", "Reason": "User has not verified thier removal"})
    return jsonify({"Status": "Fail", "Reason": "User does not exist"})

@accounts_bp.route("/api/accounts/auth/<email>/<attempt>", methods=["GET"])
def authenticate(email, attempt):
    users = db.session.query(models.User).all()
    user_id = list(filter(lambda x: x.email == email, users))[0].id
    user: models.User | None = db.session.get(models.User, user_id)
    if user: 
        if bcrypt.check_password_hash(user.password, attempt):
            return jsonify({"Status": "Success"}) 
    return jsonify({"Status": "Fail"}) 

