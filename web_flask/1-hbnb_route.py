#!/usr/bin/python3
"""
Flask web application with an additional route
"""

from flask import Flask

# Initialize the Flask application
app = Flask(__name__)

@app.route('/', strict_slashes=False)
def index():
    """Return a greeting message."""
    return 'Hello HBNB!'

@app.route('/hbnb', strict_slashes=False)
def hbnb():
    """Return a custom message."""
    return 'HBNB'

if __name__ == '__main__':
    # Run the app on the specified host and port
    app.run(host='0.0.0.0', port='5000')
