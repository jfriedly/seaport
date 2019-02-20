import logging
import math
import os

import flask
from flask import Flask
from flask import request

import fleet
import numerical


logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)
logger.debug("$PORT is " + os.getenv("PORT"))

app = Flask(__name__)


class Recommendation(object):
    recommended_fleet = []
    requested_capacity = 0
    recommended_capacity = 0

    def __init__(self, recommended_fleet, requested_capacity):
        self.recommended_fleet = recommended_fleet
        self.requested_capacity = requested_capacity
        self.recommended_capacity = sum(recommended_fleet)

@app.route("/", methods=['GET', 'POST'])
def hello():
    if request.method == 'POST':
        # TODO(jfriedly):  log initial input and validate better
        cargo = int(request.form['cargo'])
        bonus = int(request.form['bonus'])
        logger.info("New request. Cargo is %d, bonus is %d" % (cargo, bonus))
        requested_capacity = int(math.ceil(float(cargo) / bonus))
        recommended_fleet = numerical.subsetsum(fleet.all_ships, requested_capacity)
        flask.g.recommendation = Recommendation(recommended_fleet, requested_capacity)
    return flask.render_template('index.html')
