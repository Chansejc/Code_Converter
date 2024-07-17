from typing import List
from flask import Blueprint, jsonify, request, Response
from src.core import models as core_models
from src.core.models import DecompressionError
from src.accounts import models as account_models
from src import db
import zlib 
import base64 
import os, sys
import time 


core_bp = Blueprint("core", __name__)

def parseData(data):
    data = data.replace("%sp", " ")
    data = data.replace("%n", "\n")
    data = data.replace("%t", "\t")
    data = data.replace("%r", "\r")
    data = data.replace("%rn", "\r\n")
    return data

@core_bp.route("/api/core/send_payload/", methods=["POST","GET"])
def decompress_payload(): 
    try:
        data = request.json.get("data")
        print(data)
        inputLanguage = data["InputLanguage"]
        outputLanguage = data["OutputLanguage"]
        payload = data['payload'] 
        compressed = base64.b64decode(payload) 
        decompressed = zlib.decompress(compressed) 
        final_payload = decompressed.decode("utf-8")
        final_payload = parseData(final_payload)
        return jsonify( { "GPT Response": True, "InputLanguage": inputLanguage,"OutputLanguage": outputLanguage, "data": final_payload } ) 
    except Exception as e:
        print("Error occurred", e)
        return jsonify({"GPT Response": False})
