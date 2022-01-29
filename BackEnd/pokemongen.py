#!/usr/bin/env python3
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

if __name__ == "__main__":
    app.run()

def organizePokemon():
    df = pd.read_csv('pokemon.csv')
    print (df)

@app.route("/metamorph")
def metamorph():
    return {0}