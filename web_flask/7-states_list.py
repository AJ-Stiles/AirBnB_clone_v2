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

@app.route('/states_list')
def states_list():
    """Route that displays a list of states from the DBStorage."""
    states = storage.all(State).values()
    sorted_states = sorted(states, key=lambda s: s.name)

    return render_template('7-states_list.html', states=sorted_states)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)

