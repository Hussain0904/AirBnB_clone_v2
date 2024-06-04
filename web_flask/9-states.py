#!/usr/bin/python3
"""
Start a Flask web application displaying states and their cities
"""

from flask import Flask, render_template
from models import storage

app = Flask(__name__)

@app.route('/states', strict_slashes=False)
@app.route('/states/<state_id>', strict_slashes=False)
def states(state_id=None):
    """Render a template with states and their cities."""
    states
