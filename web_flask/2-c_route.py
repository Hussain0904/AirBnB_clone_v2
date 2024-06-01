#!/usr/bin/python3
"""
Flask web application with variable route
"""

from flask import Flask

# Initialize the Flask application
app = Flask(__name__)

@app.route('/', strict_slashes=False)
def index():
    """Returns a welcome message."""
    return 'Hello HBNB!'

@app.route('/hbnb', strict_slashes=False)
def hbnb():
    """Returns a special message."""
    return 'HBNB is awesome!'

@app.route('/c/<text>', strict_slashes=False)
def custom_message(text):
    """Displays a custom message with the provided text."""
    return 'Custom message: ' + text.replace('_', ' ')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port='5000')
