from flask import Flask

app = Flask(__name__)


@app.route("/")
def home_page():
    return "Hello, World!"

@app.route("/<username>")
def about_page(username):
    return f"This is {username}'s profile"