#!/usr/bin/python3
from flask import Flask

app = Flask(__name__, strict_slashes=False)

@app.route("/")
def hello_world():
    return "Hello HBNB!"