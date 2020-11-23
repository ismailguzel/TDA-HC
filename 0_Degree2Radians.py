# -*- coding: utf-8 -*-
"""
Created on Tue Oct 27 18:06:54 2020

@author: ismailguzel
"""

import math
import pandas as pd

lat_lon = pd.read_excel("Data/Coordinates_Turkey.xlsx", header=0)
lat_lon.columns

lat_lon["x"] = lat_lon.lat*(math.pi/180)
lat_lon["y"] = lat_lon.long*(math.pi/180)

lat_lon.index = lat_lon["il"]
lat_lon.drop(["il","lat","long"], axis = 1, inplace=True)

lat_lon.to_csv("Data/Original_Coordinates.csv")
