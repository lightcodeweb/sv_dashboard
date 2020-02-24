import json
from flask import Flask, send_from_directory, render_template
from .util import load_config, get_data

APP = Flask(__name__, static_folder='static', static_url_path='/static')
CFG = load_config()


def get_app():

    return APP


# Flask default route to catch all unhandled URLs
# https://stackoverflow.com/questions/13678397/python-flask-default-route-possible
@APP.route('/', defaults={'path': ''})
@APP.route('/<path:path>')
def index(path=None):
    listings = get_data()
    return render_template('index.html', listings=listings)


@APP.route('/get_csv', methods=['GET', 'POST'])
def get_csv():
    return send_from_directory(APP.static_folder, 'data.csv', as_attachment=True)
