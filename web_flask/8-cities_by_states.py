#!/usr/bin/python3
"""
A Flask application listing cities by states
"""

from flask import Flask, render_template
from models import storage

app = Flask(__name__)

@app.route('/cities_by_states', strict_slashes=False)
def list_cities_by_states():
    """Renders a template with the list of states and their cities."""
    states = storage.all("State").values()
    return render_template('8-cities_by_states.html', states=states)

@app.teardown_appcontext
def close_storage(exception):
    """Closes the storage."""
    storage.close()

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
