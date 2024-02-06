import os
import requests

from flask import Flask, request
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
    responce = requests.post(f"http://{os.getenv('POST_SERVICE_HOST')}:{os.getenv('POST_SERVICE_PORT')}/api/new_posts",
                             json=request.json,
                             headers={"Content-Type": "application/json"})
    return responce.json()


@app.put("/posts/<int:id>")
def update_posts(id):
    responce = requests.put(f"http://{os.getenv('POST_SERVICE_HOST')}:{os.getenv('POST_SERVICE_PORT')}/api/posts/{id}",
                            json=request.json,
                            headers={"Content-Type": "application/json"})
    return responce.json()
    

@app.delete("/posts/<int:id>")
def delete_posts(id):
     responce = requests.delete(f"http://{os.getenv('POST_SERVICE_HOST')}:{os.getenv('POST_SERVICE_PORT')}/api/delete_posts/{id}",
                             json=request.json,
                             headers={"Content-Type": "application/json"})
     return responce.json()
 

@app.post("/sign_up")
def sign_up():
    responce = requests.post(f"http://{os.getenv('USERS_SERVICE_HOST')}:{os.getenv('USERS_SERVICE_PORT')}/sign_up",
                             json=request.json,
                             headers={"Content-Type": "application/json"})
    return responce.json()


@app.post("/sign_in")
def sign_in():
    responce = requests.post(f"http://{os.getenv('USERS_SERVICE_HOST')}:{os.getenv('USERS_SERVICE_PORT')}/sign_in",
                             json=request.json,
                             headers={"Content-Type": "application/json"})
    return responce.json()


@app.put("/change_password")
def change_password():
    responce = requests.put(f"http://{os.getenv('USERS_SERVICE_HOST')}:{os.getenv('USERS_SERVICE_PORT')}/change_password",
                             json=request.json,
                             headers={"Content-Type": "application/json"})
    return responce.json()


@app.delete("/delete_user/<int:id>")
def delete_user(id):
    responce = requests.delete(f"http://{os.getenv('USERS_SERVICE_HOST')}:{os.getenv('USERS_SERVICE_PORT')}/delete_user/{id}")
    return responce.json()


if __name__ == "__main__":
    app.run(port=5000, debug=True)
