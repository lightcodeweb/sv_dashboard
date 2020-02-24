"""application.py -- top-level web application for sv_dashboard.
"""
from .web import get_app
# Init Flask app
APP = get_app()
