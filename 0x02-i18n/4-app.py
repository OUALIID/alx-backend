#!/usr/bin/env python3
""" A basic Flask application with one path and an HTML template. """
from flask import Flask, render_template, request
from flask_babel import Babel


class Config():
    """ Configuration class for the Flask app. """
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"


app = Flask(__name__)
babel = Babel(app)
app.config.from_object(Config)


@app.route("/")
def index():
    """ Returns Hello world """
    return render_template('4-index.html')


@babel.localeselector
def get_locale():
    """ Determine the locale for this user."""
    language = request.args.get('locale')
    if language and language in app.config['LANGUAGES']:
        return language
    return request.accept_languages.best_match(app.config["LANGUAGES"])


if __name__ == '__main__':
    app.run(host='0.0.0.0', port='5000')
