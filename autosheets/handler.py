"""handler.py implements a single AWS Lambda handler for updating Google Sheets."""
import logging
from .autosheets import Autosheets


def autosheets_handler(event, context):
    logging.basicConfig(level=logging.INFO)
    autosheets = Autosheets("./client_secrets.json")
    autosheets.update()
    return dict(status=200)
