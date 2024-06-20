from flask import Blueprint
import flask

core_bp = Blueprint("core", __name__)

@core_bp.route("/core", methods=["GET"])
def home():
    print("<Core Blueprint Reached>")
    return flask.Response("<Core Blueprint Reached>", 200)
