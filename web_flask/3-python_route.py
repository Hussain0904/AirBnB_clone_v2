#!/usr/bin/python3
"""
A Flask application with additional dynamic routes
"""

from flask import Flask

app = Flask(__name__)

@app.route('/', strict_slashes=False)
def welcome():
    """Returns a greeting."""
    return 'Hello HBNB!'

@app.route('/hbnb', strict_slashes=False)
def display_hbnb():
    """Returns HBNB string."""
    return 'HBNB'

@app.route('/c/<text>', strict_slashes=False)
def display_c(text):
    """Returns C followed by the value of the text variable."""
    formatted_text = text.replace('_', ' ')
    return f'C {formatted_text}'

@app.route('/python', strict_slashes=False)
@app.route('/python/<text>', strict_slashes=False)
def display_python(text='is cool'):
    """Returns Python followed by the value of the text variable."""
    formatted_text = text.replace('_', ' ')
    return f'Python {formatted_text}'

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
