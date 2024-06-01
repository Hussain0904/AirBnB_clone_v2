#!/usr/bin/python3
"""
Flask web application with number route and HTML template
"""

from flask import Flask, render_template

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
    return render_template('5-number.html', n=n)

@app.route('/number_template/<int:n>', strict_slashes=False)
def numbersandtemplates(n):
    """Returns an HTML page only if the variable is an integer."""
    return render_template('5-number.html', n=n)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port='5000')
