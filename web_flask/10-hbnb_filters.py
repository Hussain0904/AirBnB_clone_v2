#!/usr/bin/python3
"""
Flask web application with filters for states and amenities
"""

from flask import Flask, render_template
from models import storage

# Initialize the Flask application
app = Flask(__name__)

@app.route('/hbnb_filters', strict_slashes=False)
def filters():
    """Displays a HTML page with states and amenities for filtering."""
    states = storage.all("State").values()
    amenities = storage.all("Amenity").values()
    return render_template('10-hbnb_filters.html', states=states, amenities=amenities)

@app.teardown_appcontext
def teardown_db(exception):
    """Closes the storage on teardown."""
    storage.close()

if __name__ == '__main__':
    app.run(host='0.0.0.0', port='5000')
