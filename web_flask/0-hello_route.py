#!/usr/bin/python3
"""
Initialize Flask application
"""

from flask import Flask

app = Flask(__name__)

@app.route('/', strict_slashes=False)
def home_page():
    """Return a simple greeting."""
    return 'Welcome to HBNB!'

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
