#!/usr/bin/python3
"""This script starts a Flask web application."""

from flask import Flask, render_template
from models import storage
from models.state import State
from models.city import City
from models.amenity import Amenity

app = Flask(__name)
app.url_map.strict_slashes = False

@app.teardown_appcontext
def teardown_appcontext(exception):
    """Close the current SQLAlchemy session."""
    storage.close()

@app.route('/hbnb_filters')
def hbnb_filters():
    """Route that displays an HTML page with filters for States, Cities, and Amenities."""
    states = sorted(storage.all(State).values(), key=lambda s: s.name)
    cities = sorted(storage.all(City).values(), key=lambda c: c.name)
    amenities = sorted(storage.all(Amenity).values(), key=lambda a: a.name)

    return render_template('10-hbnb_filters.html', states=states, cities=cities, amenities=amenities)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)

