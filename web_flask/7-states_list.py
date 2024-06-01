#!/usr/bin/python3
"""
A Flask application listing states
"""

from flask import Flask, render_template
from models import storage

app = Flask(__name__)

@app.route('/states_list', strict_slashes=False)
def list_states():
    """Renders a template with the list of states."""
    states = sorted(storage.all("State").values(), key=lambda state: state.name)
    return render_template('7-states_list.html', states=states)

@app.teardown_appcontext
def close_storage(exception):
    """Closes the storage."""
    storage.close()

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
