#!/usr/bin/python3
"""
Flask web application starting point
"""

from flask import Flask

# Initialize the Flask application
app = Flask(__name__)

@app.route('/', strict_slashes=False)
def index():
    """Returns a greeting message."""
    return 'Hello, Flask!'

if __name__ == '__main__':
    app.run(host='0.0.0.0', port='5000')
