#!/usr/bin/python3
"""This script starts a Flask web application."""

from flask import Flask, render_template
from models import storage
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place

app = Flask(__name)
app.url_map.strict_slashes = False

@app.teardown_appcontext
def teardown_appcontext(exception):
    """Close the current SQLAlchemy session."""
    storage.close()

@app.route('/hbnb')
def hbnb():
    """Route that displays an HTML page like 8-index.html from the 0x01 project."""
    states = sorted(storage.all(State).values(), key=lambda s: s.name)
    cities = sorted(storage.all(City).values(), key=lambda c: c.name)
    amenities = sorted(storage.all(Amenity).values(), key=lambda a: a.name)
    places = sorted(storage.all(Place).values(), key=lambda p: p.name)

    return render_template('100-hbnb.html', states=states, cities=cities, amenities=amenities, places=places)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)

