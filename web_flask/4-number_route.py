#!/usr/bin/python3
"""
Flask application with number route
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

@app.route('/python', strict_slashes=False)
@app.route('/python/<text>', strict_slashes=False)
def python_route(text='is cool'):
    """Return text with 'Python ' prefix."""
    processed_text = text.replace('_', ' ')
    return f'Python {processed_text}'

@app.route('/number/<int:n>', strict_slashes=False)
def number_route(n):
    """Return a text stating if n is a number."""
    return f'{n} is a number'

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
