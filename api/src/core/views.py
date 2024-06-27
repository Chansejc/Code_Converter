from typing import List
from flask import Blueprint, jsonify, request
from src.accounts import models
from src import db
import os
import flask

core_bp = Blueprint("core", __name__)

@core_bp.route("/api/core/add_entry/<filename>/<email>", methods=["GET","POST"])
def query(email, filename):
    print("<Core>>Query Endpoint Reached>")
    status = "Success"
    user: None | models.User = None 
    try:
        users: List[models.User] = db.session.query(models.User).all()
        user_id : int = list(filter(lambda x: x.email == email ,users))[0].id
         
    except Exception as e:
        print("<Error Raised in [Core>>add_entry]>", e)
        status = "Fail"
    finally:
        return jsonify({
            "Status": f"{status}"
            })


