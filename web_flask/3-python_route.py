#!/usr/bin/python3
"""
Flask web application with optional variable route
"""

from flask import Flask

# Initialize the Flask application
app = Flask(__name__)

@app.route('/', strict_slashes=False)
def index():
    """Returns a simple message."""
    return 'Hello Pythonistas!'

@app.route('/hbnb', strict_slashes=False)
def hbnb():
    """Returns a custom message."""
    return 'Welcome to Python HBNB!'

@app.route('/c/<text>', strict_slashes=False)
def cisfun(text):
    """Returns a message with a custom variable."""
    return 'Custom message: ' + text.replace('_', ' ')

@app.route('/python', strict_slashes=False)
@app.route('/python/<text>', strict_slashes=False)
def pythoniscool(text='is fun'):
    """Returns a message with an optional variable."""
    return 'Python is ' + text.replace('_', ' ')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port='5000')
