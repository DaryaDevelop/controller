import os

from flask import Flask
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)


@app.get("/")
def index():
    test = f"http://{os.getenv('POST_SERVICE_HOST')}:{os.getenv('POST_SERVICE_PORT')}/new_post"
    return test


if __name__ == "__main__":

    app.run(port=5000)
