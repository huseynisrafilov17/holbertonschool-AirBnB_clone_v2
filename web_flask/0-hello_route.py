#!/usr/bin/python3
"""My Flask Task"""
from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<p>Hello, HBNB!</p>"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
