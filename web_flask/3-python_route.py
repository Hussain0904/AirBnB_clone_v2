#!/usr/bin/python3
"""
Flask web application with number route
"""

from flask import Flask

# Initialize the Flask application
app = Flask(__name__)

@app.route('/', strict_slashes=False)
def index():
    """Returns a simple message."""
    return 'Hello Numbers!'

@app.route('/hbnb', strict_slashes=False)
def hbnb():
    """Returns a custom message."""
    return 'Welcome to Numbers HBNB!'

@app.route('/c/<text>', strict_slashes=False)
def cisfun(text):
    """Returns a message with a custom variable."""
    return 'Custom message: ' + text.replace('_', ' ')

@app.route('/python', strict_slashes=False)
@app.route('/python/<text>', strict_slashes=False)
def pythoniscool(text='is cool'):
    """Returns a message with an optional variable."""
    return 'Python ' + text.replace('_', ' ')

@app.route('/number/<int:n>', strict_slashes=False)
def imanumber(n):
    """Returns a message only if the variable is an integer."""
    return "{:d} is a great number".format(n)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port='5000')
