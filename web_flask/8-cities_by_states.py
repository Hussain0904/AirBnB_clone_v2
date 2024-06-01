#!/usr/bin/python3
"""
Flask web application displaying cities by states
"""

from flask import Flask, render_template
from models import storage

# Initialize the Flask application
app = Flask(__name__)

@app.route('/cities_by_states', strict_slashes=False)
def cities_by_states():
    """Return an HTML page with states and their cities listed alphabetically."""
    states = storage.all("State").values()
    return render_template('8-cities_by_states.html', states=states)

@app.teardown_appcontext
def teardown_db(exception):
    """Close the storage on teardown."""
    storage.close()

if __name__ == '__main__':
    # Run the app on the specified host and port
    app.run(host='0.0.0.0', port='5000')
