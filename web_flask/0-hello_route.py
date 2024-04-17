#!/usr/bin/python3
from flask import Flask
"""
task 0
"""


app = Flask(__name__, strict_slashes=False)

@app.route("/")
def hello_world():
    """default page"""
    return "Hello HBNB!"

if __name__ == '__main__':
      app.run(host='0.0.0.0', port=5000)