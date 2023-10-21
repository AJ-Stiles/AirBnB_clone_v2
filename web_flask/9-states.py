#!/usr/bin/python3
"""This script starts a Flask web application."""

from flask import Flask, render_template
from models import storage
from models.state import State
from models.city import City

app = Flask(__name)
app.url_map.strict_slashes = False

@app.teardown_appcontext
def teardown_appcontext(exception):
    """Close the current SQLAlchemy session."""
    storage.close()

@app.route('/states')
def states():
    """Route that displays a list of states from DBStorage."""
    states = storage.all(State).values()
    sorted_states = sorted(states, key=lambda s: s.name)

    return render_template('9-states.html', states=sorted_states)

@app.route('/states/<id>')
def state_cities(id):
    """Route that displays a list of cities for a specific state from DBStorage."""
    state = storage.get(State, id)
    if state:
        cities = sorted(state.cities, key=lambda c: c.name)
        return render_template('9-states.html', state=state, cities=cities)
    else:
        return render_template('9-states.html', not_found=True)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)

