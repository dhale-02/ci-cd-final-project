"""Accounts Service"""
from flask import Flask
from flask_talisman import Talisman
from flask_cors import CORS

app = Flask(__name__)

# Security headers with Talisman
talisman = Talisman(app)

# CORS policies
CORS(app)

from service import routes  # noqa: E402, F401
