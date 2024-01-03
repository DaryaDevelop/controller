import os
import requests

from flask import Flask
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)


@app.get("/posts")
def all_posts():
    test = f"http://{os.getenv('POST_SERVICE_HOST')}:{os.getenv('POST_SERVICE_PORT')}/api/all_posts"
    response = requests.get(test)
    return response.json()


@app.post("/new_posts")
def new_posts():
    responce = requests.get(f"http://{os.getenv('POST_SERVICE_HOST')}:{os.getenv('POST_SERVICE_PORT')}/api/new_posts")
    return responce.json()


@app.put("/posts/<int:id>")
def update_posts(id):
    responce = requests.get(f"http://{os.getenv('POST_SERVICE_HOST')}:{os.getenv('POST_SERVICE_PORT')}/api/posts/<int:id")
    return responce.json()
    

@app.delete("/posts/<int:id>")
def delete_posts(id):
     responce = requests.get(f"http://{os.getenv('POST_SERVICE_HOST')}:{os.getenv('POST_SERVICE_PORT')}/api/delete_posts/<int:id")
     return responce.json()
 
     
if __name__ == "__main__":
    app.run(port=5000)
