#!/usr/bin/python3
"""
Start a Flask web application to list cities by states
"""

from flask import Flask, render_template
from models import storage

app = Flask(__name__)

@app.route('/cities_by_states', strict_slashes=False)
def cities_by_states():
    """Render a template with the list of states and their cities."""
    states = storage.all("State").values()
    return render_template('8-cities_by_states.html', states=states)


@app.teardown_appcontext
def teardown_db(exception):
    """Close the storage on teardown."""
    storage.close()


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
