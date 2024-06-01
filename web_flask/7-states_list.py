#!/usr/bin/python3
"""
Start a Flask web application to list states
"""

from flask import Flask, render_template
from models import storage

app = Flask(__name__)

@app.route('/states_list', strict_slashes=False)
def states_list():
    """Render a template with the list of states."""
    states = sorted(storage.all("State").values(), key=lambda state: state.name)
    return render_template('7-states_list.html', states=states)

@app.teardown_appcontext
def teardown_db(exception):
    """Close the storage on teardown."""
    storage.close()

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
