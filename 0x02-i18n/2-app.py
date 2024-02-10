#!/usr/bin/env python3
""" A basic Flask application with one path and an HTML template. """
from flask import Flask, render_template, request
from flask_babel import Babel
app = Flask(__name__)
babel = Babel(app)


@babel.localeselector
def get_locale():
    """ Determine the locale for this user."""
    return request.accept_languages.best_match()


@app.route('/')
def index():
    """ Returns Hello world """
    return render_template('2-index.html')


if __name__ == '__main__':
    app.run(host='127.0.0.1', port='5000')
