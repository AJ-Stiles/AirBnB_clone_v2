#!/usr/bin/python3
"""This script starts a Flask web application."""

from flask import Flask, render_template
from models import storage
from models.state import State

app = Flask(__name)
app.url_map.strict_slashes = False

@app.teardown_appcontext
def teardown_appcontext(exception):
    """Close the current SQLAlchemy session."""
    storage.close()

@app.route('/cities_by_states')
def cities_by_states():
    """Route that displays a list of states and their cities from DBStorage."""
    states = storage.all(State).values()
    sorted_states = sorted(states, key=lambda s: s.name)

    return render_template('8-cities_by_states.html', states=sorted_states)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)

