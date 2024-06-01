#!/usr/bin/python3
"""
Flask web application with states and state-specific route
"""

from flask import Flask, render_template
from models import storage

# Initialize the Flask application
app = Flask(__name__)

@app.route('/states', strict_slashes=False)
@app.route('/states/<state_id>', strict_slashes=False)
def states(state_id=None):
    """Return an HTML page with states and optionally a specific state."""
    states = storage.all("State")
    state_id = 'State.' + state_id if state_id else None
    return render_template('9-states.html', states=states, state_id=state_id)

@app.teardown_appcontext
def teardown_db(exception):
    """Close the storage on teardown."""
    storage.close()

if __name__ == '__main__':
    # Run the app on the specified host and port
    app.run(host='0.0.0.0', port='5000')
