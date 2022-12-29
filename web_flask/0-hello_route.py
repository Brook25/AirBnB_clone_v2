#!/usr/bin/env python3
"""A script that starts a Flask web_app"""
from flask import Flask

app = Flask(__name__)
@app.route('/', strict_slashes=False)
def first_page():
    """displays a string on '/'"""
    return "Hello HBNB!"

if __name__ == "__main__":
    app.run(host="0.0.0.0")
