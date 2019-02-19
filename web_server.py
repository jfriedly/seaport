import logging
import os

import flask
from flask import Flask
from flask import request


logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)
logger.debug("$PORT is " + os.getenv("PORT"))

app = Flask(__name__)


class Recommendation(object):
    requested_capacity = 0
    recommended_capacity = 0
    fleet = []

    def __init__(self, requested_capacity, fleet):
        self.requested_capacity = requested_capacity
        self.recommended_capacity = sum(fleet)
        self.fleet = fleet

@app.route("/", methods=['GET', 'POST'])
def hello():
    if request.method == 'GET':
        return flask.render_template('index.html')
    else:
        flask.g.recommendation = Recommendation(42, [21, 21])
        return flask.render_template('index.html')
