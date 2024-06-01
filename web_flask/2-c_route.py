#!/usr/bin/python3
"""
Flask web application with variable route
"""

from flask import Flask

# Initialize the Flask application
app = Flask(__name__)

@app.route('/', strict_slashes=False)
def index():
    """Return a simple message."""
    return 'Hello HBNB!'

@app.route('/hbnb', strict_slashes=False)
def hbnb():
    """Return a custom message."""
    return 'HBNB'

@app.route('/c/<text>', strict_slashes=False)
def cisfun(text):
    """Return a message with a custom variable."""
    return 'C ' + text.replace('_', ' ')

if __name__ == '__main__':
    # Run the app on the specified host and port
    app.run(host='0.0.0.0', port='5000')
