# -*- coding: utf-8 -*-
"""
Created on Wed Oct 28 10:15:22 2020

@author: ismailguzel
"""

import numpy as np
import pandas as pd
import gudhi as gd
import json


Dataset = pd.read_csv("Data/Original_Coordinates.csv")
Dataset.index = Dataset["il"]
Dataset = Dataset.drop("il", axis=1)
Dataset = Dataset.iloc[:24,]
pt_cloud = np.c_[Dataset["x"].values, Dataset["y"].values]

rips_complex = gd.RipsComplex(pt_cloud, max_edge_length = .5)
simplex_tree = rips_complex.create_simplex_tree(max_dimension = 2)

L = simplex_tree.get_filtration()

my_data =[list(simplex) for simplex in L]


with open("Outputs/simplex_with_epsilon.txt", "w") as file:  # save the simplices with epsilon to use in SageMath
    file.write(json.dumps(my_data))
file.close()