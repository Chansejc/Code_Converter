from flask import Blueprint, request
from src import db
from src import bcrypt
import flask

# Blueprint todos:
## When queries are sent to the server from the client should I encrypt the URL that is being used--
##      then decrypt the message on the server side.

accounts_bp = Blueprint("accounts", __name__)

@accounts_bp.route("/accounts", methods=["GET"])
def home():
    print("<Accounts Blueprint Reached>")
    return flask.jsonify({ "<Accounts Blueprint Reached>": True })

@accounts_bp.route("/accounts/new", methods=["GET"])
def new():
    print("<Accounts (New) Blueprint Reached>")
    creds = request.args.get('username'),request.args.get('password') #Username, Password
    
    if len(list(filter(lambda i: type(i) != type(None), creds))) == 2:
        print("<Required Parameters Accepted>")
    else:
        return flask.jsonify({"Creation Status": "Fail", "username": creds[0], "password": creds[1] })

    return flask.jsonify({"Creation Status": "Success", "Username": creds[0], "Password": creds[1] })

@accounts_bp.route("/accounts/remove", methods=["GET"])
def remove():
    print("<Accounts (Remove) Blueprint Reached>")
    creds = request.args.get('username'), request.args.get('password') #Username, Password

    if len(list(filter(lambda i: type(i) != type(None), creds))) == 2:
        print("<Required Parameters Accepted>")
    else:
        return flask.jsonify({"Removal Status": "Fail", "username": creds[0], "password": creds[1] })

    return flask.jsonify({"Removal Status": "Success", "Username": creds[0], "Password": creds[1] })

