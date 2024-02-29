import os
from functools import wraps

import requests
from flask import request


def check_login(func):
    @wraps(func)
    def wraper(*args, **kwargs):
        uuid = request.headers.get("Authorization")
        if not uuid:
            return {
                "status": 7,
                "description": "UUid not found",
                "data": {}
            }, 400
        uuid = uuid.split(" ")
        if len(uuid) != 2:
            return {
                "status": 8,
                "description": "Invalid data",
                "data": {}
            }, 400
        responce = requests.get(f"http://{os.getenv('DB_SERVICE_HOST')}:{os.getenv('DB_SERVICE_PORT')}/check_login/{uuid[1]}")
        if responce.status_code == 200:
            return func(*args, **kwargs)
        else:
            return {
                "status": 6,
                "description": "User not found",
                "data": {}
            }, 401
    return wraper
