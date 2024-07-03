from typing import List
from flask import Blueprint, jsonify, request
from src.core import models as core_models
from src.core.models import DecompressionError
from src.accounts import models as account_models
from src import db
import zlib 
import base64 
import os, sys
import time 


core_bp = Blueprint("core", __name__)

@core_bp.route("/api/core/rec_file/<email>/<data>", methods=["GET","POST"])
def decompress_data(email, data): #a function with the parameters Email and Data
    decompression_status = {"data": "No Data", 'error': "No Error"} # Hashmap tracking the status of the function
    try:
        start: int = time.time_ns()
        user_id: int = account_models.get_user(email, account_models.User).id
        data = data.replace("+", "/")
        print(data)
        compressed = base64.b64decode(data)
        decompressed = zlib.decompress(compressed).decode("utf-8")
        print("User_id :\n", user_id)
        filename = core_models.genFilename()

        if str(user_id) not in os.listdir("./smorg/"): 
            os.mkdir(f"./smorg/{user_id}")
        else: 
            if filename not in os.listdir(f"./smorg/{user_id}"):
                with open(f"./smorg/{user_id}/{filename}", "wb") as f:
                    print(decompressed)
                    f.write(decompressed)
        decompression_status['data'] = "Success"
        end: int = time.time_ns()
        print("This operation took: ", (end - start))

    # [DecompressionError.Value, DecompressionError.zlib, DecompressionError.UserNotFound, 
    #         FileNotFoundError, TypeError] 
    except Exception as e:
        print(e)
        raise e
        # match e:
        #     case DecompressionError.Type:
        #         decompression_status["error"] =  "TypeError"
        #     case DecompressionError.File:
        #         decompression_status["error"] =  "FileNotFoundError"
        #     case DecompressionError.UserNotFound:
        #         decompression_status["error"] =  "UserNotFound"
        #     case DecompressionError.zlib:
        #         decompression_status["error"] =  "Decompression"
        #     case DecompressionError.Value:
        #         decompression_status["error"] =  "Decoding"
        #     case _:
        #         decompression_status["error"] =  "Unknown"
    finally:
        return jsonify(decompression_status)
