#!/usr/bin/python3
"""This script starts a Flask web application."""

from flask import Flask, render_template

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
    """Route that displays 'C ' followed by the value of the text variable."""
    # Replace underscores with spaces in the text variable
    text = text.replace("_", " ")
    return 'C {}'.format(text)

@app.route('/python/', defaults={'text': 'is cool'}, strict_slashes=False)
@app.route('/python/<text>', strict_slashes=False)
def python_text(text):
    """Route that displays 'Python ' followed by the value of the text variable (default: 'is cool')."""
    # Replace underscores with spaces in the text variable
    text = text.replace("_", " ")
    return 'Python {}'.format(text)

@app.route('/number/<int:n>', strict_slashes=False)
def is_number(n):
    """Route that displays 'n is a number' only if n is an integer."""
    return '{} is a number'.format(n)

@app.route('/number_template/<int:n>', strict_slashes=False)
def number_template(n):
    """Route that displays an HTML page with the number."""
    return render_template('7-number.html', n=n)

@app.route('/number_odd_or_even/<int:n>', strict_slashes=False)
def number_odd_or_even(n):
    """Route that displays an HTML page with the number and its even/odd status."""
    return render_template('8-number_odd_or_even.html', n=n)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)

