#!/usr/bin/python3
"""
A Flask application with number parity check and template rendering
"""

from flask import Flask, render_template

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

@app.route('/number/<int:n>', strict_slashes=False)
def display_number(n):
    """Returns n is a number only if n is an integer."""
    return f'{n} is a number'

@app.route('/number_template/<int:n>', strict_slashes=False)
def display_number_template(n):
    """Renders a template only if n is an integer."""
    return render_template('5-number.html', number=n)

@app.route('/number_odd_or_even/<int:n>', strict_slashes=False)
def display_number_odd_or_even(n):
    """Renders a template to show if n is odd or even."""
    even_or_odd = 'even' if n % 2 == 0 else 'odd'
    return render_template('6-number_odd_or_even.html', number=n, even_or_odd=even_or_odd)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
