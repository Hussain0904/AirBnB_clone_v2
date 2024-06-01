#!/usr/bin/python3
"""
Flask application with number, odd or even route
"""

from flask import Flask, render_template

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

@app.route('/number/<int:n>', strict_slashes=False)
def show_number(n):
    """Displays 'n is a number' only if n is an integer."""
    return f"{n} is a number"

@app.route('/number_template/<int:n>', strict_slashes=False)
def show_number_template(n):
    """Displays a HTML page only if n is an integer."""
    return render_template('5-number.html', n=n)

@app.route('/number_odd_or_even/<int:n>', strict_slashes=False)
def show_number_odd_or_even(n):
    """Displays a HTML page only if n is an integer, showing if it's odd or even."""
    evenness = 'even' if n % 2 == 0 else 'odd'
    return render_template('6-number_odd_or_even.html', n=n, evenness=evenness)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
