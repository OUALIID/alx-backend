#!/usr/bin/env python3
""" A basic Flask application with one path and an HTML template. """
from flask import Flask, render_template
app = Flask(__name__)


@app.route('/')
def index():
    """ Returns Hello world """
    return render_template('0-index.html')


if __name__ == '__main__':
    app.run(host='127.0.0.1', port='5000')
