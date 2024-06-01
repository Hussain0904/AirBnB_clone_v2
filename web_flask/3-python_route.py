#!/usr/bin/python3
"""
Flask application with multiple dynamic routes
"""

from flask import Flask

app = Flask(__name__)

@app.route('/', strict_slashes=False)
def home():
    """Returns a greeting."""
    return 'Hello HBNB!'

@app.route('/hbnb', strict_slashes=False)
def hbnb_page():
    """Returns 'HBNB'."""
    return 'HBNB'

@app.route('/c/<text>', strict_slashes=False)
def show_c_message(text):
    """Displays 'C ' followed by the text variable."""
    return 'C ' + text.replace('_', ' ')

@app.route('/python', strict_slashes=False)
@app.route('/python/<text>', strict_slashes=False)
def show_python_message(text='is cool'):
    """Displays 'Python ' followed by the text variable."""
    return 'Python ' + text.replace('_', ' ')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
