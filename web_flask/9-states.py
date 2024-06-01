#!/usr/bin/python3
"""
Flask application displaying states and their cities
"""

from flask import Flask, render_template
from models import storage

app = Flask(__name__)

@app.route('/states', strict_slashes=False)
@app.route('/states/<state_id>', strict_slashes=False)
def display_states(state_id=None):
    """Render a template with states and their cities."""
    states = storage.all("State")
    if state_id:
        state_id = 'State.' + state_id
    return render_template('9-states.html', states=states, state_id=state_id)

@app.teardown_appcontext
def close_storage(exception):
    """Close the storage."""
    storage.close()

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
