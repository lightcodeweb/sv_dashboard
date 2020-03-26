import json
from flask import Flask, send_from_directory, render_template, request
from .util import get_event_list, load_config, generate_csv
from .database import Database

APP = Flask(__name__, static_folder='static', static_url_path='/static')
CFG = load_config()


def get_app():
    return APP


@APP.route('/', defaults={'path': ''})
@APP.route('/<path:path>')
def index(path=None):
    db = Database(CFG)

    s_listings = db.get_listings_by_brand("0")
    v_listings = db.get_listings_by_brand("1")
    return render_template('index.html', s_listings=s_listings, v_listings=v_listings)


@APP.route('/get_events', methods=['POST'])
def get_events():
    return json.dumps({
        "success": True,
        "events": get_event_list()
    })


@APP.route('/save_listings', methods=['POST'])
def save_listings():
    json_data = request.get_json()
    listings = json_data.get("listings")
    should_reset = json_data.get("should_reset")

    db = Database(CFG)

    if should_reset:
        db.remove_all_listings()

    for listing in listings:
        db.save_data(
            listing["title"],
            listing["price"],
            listing["section"],
            listing["num"],
            listing["row"],
            listing["quantity"],
            listing["brand"],
            listing["url"]
        )

    return json.dumps({
        "success": True
    })


@APP.route('/get_csv', methods=['GET', 'POST'])
def get_csv():
    generate_csv()
    return send_from_directory(APP.static_folder, 'output.csv', as_attachment=True)
