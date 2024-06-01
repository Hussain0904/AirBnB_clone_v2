#!/usr/bin/python3
"""
Flask web application with an additional route
"""

from flask import Flask

# Initialize the Flask application
app = Flask(__name__)

@app.route('/', strict_slashes=False)
def index():
    """Returns a welcome message."""
    return 'Welcome to HBNB!'

@app.route('/hbnb', strict_slashes=False)
def hbnb():
    """Returns a special message."""
    return 'HBNB is amazing!'

if __name__ == '__main__':
    app.run(host='0.0.0.0', port='5000')
