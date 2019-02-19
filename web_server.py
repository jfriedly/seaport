import logging
import os

from flask import Flask

logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)
logger.debug("$PORT is " + os.getenv("PORT"))

app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello world!"
