#!/usr/bin/python3
"""
Flask application with odd or even number route
"""

from flask import Flask, render_template

app = Flask(__name__)

@app.route('/', strict_slashes=False)
def home_page():
    """Return a simple greeting."""
    return 'Welcome to HBNB!'

@app.route('/hbnb', strict_slashes=False)
def hbnb():
    """Return HBNB text."""
    return 'HBNB'

@app.route('/c/<text>', strict_slashes=False)
def c_route(text):
    """Return text with 'C ' prefix."""
    processed_text = text.replace('_', ' ')
    return f'C {processed_text}'

@app.route('/python', strict_slashes=False)
@app.route('/python/<text>', strict_slashes=False)
def python_route(text='is cool'):
    """Return text with 'Python ' prefix."""
    processed_text = text.replace('_', ' ')
    return f'Python {processed_text}'

@app.route('/number/<int:n>', strict_slashes=False)
def number_route(n):
    """Return a text stating if n is a number."""
    return f'{n} is a number'

@app.route('/number_template/<int:n>', strict_slashes=False)
def number_template_route(n):
    """Render a template only if n is an integer."""
    return render_template('5-number.html', number=n)

@app.route('/number_odd_or_even/<int:n>', strict_slashes=False)
def odd_or_even_route(n):
    """Render a template to show if the number is odd or even."""
    evenness = 'even' if n % 2 == 0 else 'odd'
    return render_template('6-number_odd_or_even.html', number=n, evenness=evenness)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)