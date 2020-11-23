# -*- coding: utf-8 -*-
"""
Created on Thu Oct 29 16:19:37 2020

@author: ismailguzel
"""
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

##################### DIONYSUS ####################################
dionysus_bd = pd.read_csv("Outputs\dionysus_bd.csv")
dionysus_bd.drop('Unnamed: 0', axis=1, inplace=True)
dionysus_bd = pd.DataFrame(np.where(dionysus_bd == np.inf, 10, dionysus_bd),columns=dionysus_bd.columns)
dionysus_bd_0 = dionysus_bd[dionysus_bd.dimension == 0].drop("dimension",axis=1)
original_data = pd.read_csv("Data\Original_Coordinates.csv")
cities = original_data.il.values[:24]

fig, ax = plt.subplots(1, 1, figsize=(8,8), constrained_layout=True)
ax.tick_params('y', length=2, width=2, which='major', labelsize=22)
ax.tick_params('x', length=7, width=2, which='major', labelsize=22)
ax.yaxis.set_ticks(np.arange(1,25,1))
ax.yaxis.set_ticklabels(cities)
ax.set_xlim(0,0.1)
ax.spines['right'].set_visible(False)
ax.spines['top'].set_visible(False)
i=1
for time in range(len(dionysus_bd_0)):
    x = np.linspace(dionysus_bd_0.Birth[time], dionysus_bd_0.Death[time],10)
    y =np.ones(10)*i
    ax.plot(x,y,color='purple',lw=4)
    i += 1

plt.savefig('Outputs/barcode_H0_dionysus.png', dpi=500, bbox_inches='tight',pad_inches = 0.1)



##################### GUDHI ####################################
gudhi_bd = pd.read_csv("Outputs\gudhi_bd.csv")
gudhi_bd.drop('Unnamed: 0', axis=1, inplace=True)
gudhi_bd = pd.DataFrame(np.where(gudhi_bd == np.inf, 10, gudhi_bd),columns=gudhi_bd.columns)
gudhi_bd_0 = gudhi_bd[gudhi_bd.dimension == 0].drop("dimension",axis=1)


fig, ax = plt.subplots(1, 1, figsize=(8,8), constrained_layout=True)
ax.tick_params('y', length=2, width=2, which='major', labelsize=22)
ax.tick_params('x', length=7, width=2, which='major', labelsize=22)
ax.yaxis.set_ticks(np.arange(1, 25, 1))
ax.set_xlim(0,0.1)
ax.spines['right'].set_visible(False)
ax.spines['top'].set_visible(False)
i=1
for time in range(len(gudhi_bd_0)):
    x = np.linspace(gudhi_bd_0.Birth[time], gudhi_bd_0.Death[time],10)
    y =np.ones(10)*i
    ax.plot(x,y,color='blue',lw=4)
    i += 1

plt.savefig('Outputs/barcode_H0_gudhi.png', dpi=500, bbox_inches='tight',pad_inches = 0.1)