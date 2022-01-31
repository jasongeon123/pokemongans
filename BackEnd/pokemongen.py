#!/usr/bin/env python3
import sys
from flask import Flask
from flask_cors import CORS, cross_origin
from api.HelloApiHandler import HelloApiHandler
import csv
import pandas as pd
import warnings
import numpy as np
import sklearn
import os


warnings.filterwarnings("ignore")

app = Flask(__name__, static_url_path='',static_folder='frontend/build')
CORS(app)



def organizePokemon():
    df = pd.read_csv('pokemon.csv')
    df=df.astype(str)
    df1 = df[["Name","Type1"]]
    df2 = df[["Name","Type2"]]
    df2 = df2[df2["Type2"] != 'nan']
    grass1 = df1[df1["Type1"]=='Grass']
    grass1 = grass1['Name'].to_numpy()
    bug1 = df1[df1["Type1"]=='Bug']
    bug1 = bug1['Name'].to_numpy()
    dark1 = df1[df1["Type1"]=='Dark']
    dark1 = dark1['Name'].to_numpy()
    dragon1 = df1[df1["Type1"]=='Dragon']
    dragon1 = dragon1['Name'].to_numpy()
    electric1 = df1[df1["Type1"]=='Electric']
    electric1 = electric1['Name'].to_numpy()
    fairy1 = df1[df1["Type1"]=='Fairy']
    fairy1 = fairy1['Name'].to_numpy()
    fighting1 = df1[df1["Type1"]=='Fighting']
    fighting1 = fighting1['Name'].to_numpy()
    fire1 = df1[df1["Type1"]=='Fire']
    fire1 = fire1['Name'].to_numpy()
    flying1 = df1[df1["Type1"]=='Flying']
    flying1 = flying1['Name'].to_numpy()
    ghost1 = df1[df1["Type1"]=='Ghost']
    ghost1 = ghost1['Name'].to_numpy()
    ground1 = df1[df1["Type1"]=='Ground']
    ground1 = ground1['Name'].to_numpy()
    ice1 = df1[df1["Type1"]=='Ice']
    ice1 = ice1['Name'].to_numpy()
    normal1 = df1[df1["Type1"]=='Normal']
    normal1 = normal1['Name'].to_numpy()
    poison1 = df1[df1["Type1"]=='Poison']
    poison1 = poison1['Name'].to_numpy()
    psychic1 = df1[df1["Type1"]=='Psychic']
    psychic1 = psychic1['Name'].to_numpy()
    rock1 = df1[df1["Type1"]=='Rock']
    rock1 = rock1['Name'].to_numpy()
    steel1 = df1[df1["Type1"]=='Steel']
    steel1 = steel1['Name'].to_numpy()
    water1 = df1[df1["Type1"]=='Water']
    water1 = water1['Name'].to_numpy()
    grass2 = df2[df2["Type2"]=='Grass']
    grass2 = grass2['Name'].to_numpy()
    bug2 = df2[df2["Type2"]=='Bug']
    bug2 = bug2['Name'].to_numpy()
    dark2 = df2[df2["Type2"]=='Dark']
    dark2 = dark2['Name'].to_numpy()
    dragon2 = df2[df2["Type2"]=='Dragon']
    dragon2 = dragon2['Name'].to_numpy()
    electric2 = df2[df2["Type2"]=='Electric']
    electric2 = electric2['Name'].to_numpy()
    fairy2 = df2[df2["Type2"]=='Fairy']
    fairy2 = fairy2['Name'].to_numpy()
    fighting2 = df2[df2["Type2"]=='Fighting']
    fighting2 = fighting2['Name'].to_numpy()
    fire2 = df2[df2["Type2"]=='Fire']
    fire2 = fire2['Name'].to_numpy()
    flying2 = df2[df2["Type2"]=='Flying']
    flying2 = flying2['Name'].to_numpy()
    ghost2 = df2[df2["Type2"]=='Ghost']
    ghost2 = ghost2['Name'].to_numpy()
    ground2 = df2[df2["Type2"]=='Ground']
    ground2 = ground2['Name'].to_numpy()
    ice2 = df2[df2["Type2"]=='Ice']
    ice2 = ice2['Name'].to_numpy()
    normal2 = df2[df2["Type2"]=='Normal']
    normal2 = normal2['Name'].to_numpy()
    poison2 = df2[df2["Type2"]=='Poison']
    poison2 = poison2['Name'].to_numpy()
    psychic2 = df2[df2["Type2"]=='Psychic']
    psychic2 = psychic2['Name'].to_numpy()
    rock2 = df2[df2["Type2"]=='Rock']
    rock2 = rock2['Name'].to_numpy()
    steel2 = df2[df2["Type2"]=='Steel']
    steel2 = steel2['Name'].to_numpy()
    water2 = df2[df2["Type2"]=='Water']
    water2 = water2['Name'].to_numpy()
    bug = np.concatenate((bug1,bug2))
    dark = np.concatenate((dark1,dark2))
    dragon = np.concatenate((dragon1,dragon2))
    electric = np.concatenate((electric1,electric2))
    fairy = np.concatenate((fairy1,fairy2))
    fighting= np.concatenate((fighting1,fighting2))
    fire= np.concatenate((fire1,fire2))
    flying = np.concatenate((flying1,flying2))
    ghost = np.concatenate((ghost1,ghost2))
    grass= np.concatenate((grass1,grass2))
    ground = np.concatenate((ground1,ground2))
    ice = np.concatenate((ice1,ice2))
    normal = np.concatenate((normal1,normal2))
    poison= np.concatenate((poison1,poison2))
    psychic = np.concatenate((psychic1,psychic2))
    rock = np.concatenate((rock1,rock2))
    steel = np.concatenate((steel1,steel2))
    water = np.concatenate((water1,water2))
    pokemon={
        "bug":bug,
        "dark":dark,
        "dragon":dragon,
        "electric":electric,
        "fairy":fairy,
        "fighting":fighting,
        "fire":fire,
        "flying":flying,
        "ghost":ghost,
        "grass":grass,
        "ground":ground,
        "ice":ice,
        "normal":normal,
        "poison":poison,
        "psychic":psychic,
        "rock":rock,
        "steel":steel,
        "water":water
    }
    return pokemon

@app.route("/metamorph")
def pokemongenerator():
    return {0}

if __name__ == "__main__":
    app.run()