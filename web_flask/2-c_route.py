#!/usr/bin/python3
"""This script starts a Flask web application."""

from flask import Flask

app = Flask(__name)

@app.route('/', strict_slashes=False)
def hello_hbnb():
    """Route that displays 'Hello HBNB!'."""
    return 'Hello HBNB!'

@app.route('/hbnb', strict_slashes=False)
def hbnb():
    """Route that displays 'HBNB'."""
    return 'HBNB'

@app.route('/c/<text>', strict_slashes=False)
def c_text(text):
    """Route that displays 'C' followed by the value of the text variable."""
    # Replace underscores with spaces in the text variable
    text = text.replace("_", " ")
    return 'C {}'.format(text)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)

