#!/usr/bin/python3
"""
Flask web application with states list
"""

from flask import Flask, render_template
from models import storage

# Initialize the Flask application
app = Flask(__name__)

@app.route('/states_list', strict_slashes=False)
def states_list():
    """Return an HTML page with the states listed alphabetically."""
    states = sorted(list(storage.all("State").values()), key=lambda x: x.name)
    return render_template('7-states_list.html', states=states)

@app.teardown_appcontext
def teardown_db(exception):
    """Close the storage on teardown."""
    storage.close()

if __name__ == '__main__':
    # Run the app on the specified host and port
    app.run(host='0.0.0.0', port='5000')
