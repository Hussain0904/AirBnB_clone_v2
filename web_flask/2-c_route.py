#!/usr/bin/python3
"""
Flask application with dynamic route
"""

from flask import Flask

app = Flask(__name__)

@app.route('/', strict_slashes=False)
def home_page():
    """Return a simple greeting."""
    return 'Welcome to HBNB!'

@app.route('/hbnb', strict_slashes=False)
def hbnb():
    """Return HBNB text."""
    return 'HBNB'

@app.route('/c/<text>', strict_slashes=False)
def c_route(text):
    """Return text with 'C ' prefix."""
    processed_text = text.replace('_', ' ')
    return f'C {processed_text}'

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
