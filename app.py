from flask import Flask
from flask import request
from flask_restful import Api
import pandas as pd
import json
from types import SimpleNamespace

from pvlib.pvsystem import PVSystem #, retrieve_sam
from pvlib.temperature import TEMPERATURE_MODEL_PARAMETERS
from pvlib.modelchain import ModelChain
from pvlib.location import Location

app = Flask(__name__)

@app.route('/hello', methods = ['POST'])
def hello():
    data = request.get_json(silent=True)
    return "data", 200

