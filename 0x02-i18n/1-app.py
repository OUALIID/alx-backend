#!/usr/bin/env python3
""" A basic Flask application with one path and an HTML template. """
from flask import Flask, render_template
from flask_babel import Babel


class Config(object):
    """ Configuration class for the Flask app. """
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"


app = Flask(__name__)
babel = Babel(app)
app.config.from_object(Config)


@app.route('/')
def index():
    """ Returns Hello world """
    return render_template('1-index.html')


if __name__ == '__main__':
    app.run(host='127.0.0.1', port='5000')
