"""sv_dashboard Utility methods
"""
import os
import logging
import csv
import yaml
from pathlib import Path
from .database import Database


def load_config():
    """Load conf file defined by ENV var FLORIDA_SOS_CONF.
    If not available load ./conf.yaml
    """
    config = {}
    try:
        cfg_file = os.environ.get('SV_CONF')
        if not cfg_file:
            cfg_file = os.getcwd() + '/conf.yml'
            logging.warning('using default configuration from %s', cfg_file)
        with open(cfg_file, 'rt') as cfg:
            config = yaml.safe_load(cfg.read())
            logging.debug('config=%s', config)
    except IOError:
        logging.error('Error loading configuration', exc_info=1)
    return config


def get_event_list():
    input_file = os.path.join(os.path.dirname(__file__), os.pardir, "input.csv")
    path = Path(input_file)

    if not path.is_file():
        return []

    with open(input_file, "r") as file:
        reader = csv.reader(file)
        events = []

        for row in reader:
            events.append(row[0])

        return events


def generate_csv():
    db = Database(load_config())
    listings = []
    s_listings = db.get_listings_by_brand("0")
    v_listings = db.get_listings_by_brand("1")
    listings.extend(s_listings)
    listings.extend(v_listings)

    output_file = os.path.join(os.path.dirname(__file__), "static", "output.csv")

    with open(output_file, "w") as file:
        writer = csv.writer(file)
        for listing in listings:
            writer.writerow([
                listing["title"],
                listing["price"],
                listing["section"],
                listing["row"],
                listing["quantity"],
                listing["num"],
                listing["url"]
            ])

    return

