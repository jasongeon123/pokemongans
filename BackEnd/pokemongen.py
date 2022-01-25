from flask import Flask
from flask_cors import CORS, cross_origin
import csv
import pandas as pd
import warnings
import numpy as np
import sklearn
import os
import sys

warnings.filterwarnings("ignore")

app = Flask(__name__)
CORS(app)

@app.route("/metamorph")
def metamorph():
    return {0}