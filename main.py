import os
import requests

from flask import Flask
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)


@app.get("/posts")
def all_posts():
    test = f"http://{os.getenv('POST_SERVICE_HOST')}:{os.getenv('POST_SERVICE_PORT')}/api/all_post"
    response = requests.get(test)
    return response


if __name__ == "__main__":
    app.run(port=5000)
