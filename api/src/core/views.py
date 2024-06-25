from flask import Blueprint, jsonify, request
from src.accounts import models
from src import db
import os
import flask

core_bp = Blueprint("core", __name__)

@core_bp.route("/api/core/email_available/<email>/", methods=["GET"])
def test(email):
    return jsonify(True) 

@core_bp.route("/api/core/getquery", methods=["GET"])
def query():
    print("<Core (Query) Blueprint Reached>")
    content: str = ""
    try:
        with open("/mnt/c/MyStuff/projects/converter/api/src/assets/query_buffer.txt", "r") as f:
            content = f.read()
    except FileNotFoundError as e:
        print("<Location-> Core/Query>\n<Error Reading Query Buffer File>\n", e)
    finally:
        return jsonify({
            "Data": content
            })

@core_bp.route("/api/core/savefile", methods=["GET"])
def savefile():
    user = request.args.get("username")
    print("<Core Blueprint Reached>")
    return flask.Response("<Core Blueprint Reached>", 200)


