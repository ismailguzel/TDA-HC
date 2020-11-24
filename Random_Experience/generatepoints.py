import gudhi as gd
import numpy as np
import pandas as pd
import json
import sys

numrows = int(sys.argv[1])
numcolumns = int(sys.argv[2])
filenumber = int(sys.argv[3])

pt_cloud = np.random.random((numrows,numcolumns))
originpoints = pd.DataFrame(pt_cloud)
filename_output_original = "{}{}.txt".format("Outputs/output_original_",filenumber)
originpoints.to_csv(filename_output_original)


rips_complex = gd.RipsComplex(pt_cloud, max_edge_length = 1)
simplex_tree = rips_complex.create_simplex_tree(max_dimension = 2)

L = simplex_tree.get_filtration()

my_data =[list(simplex) for simplex in L]

filename_output = "{}{}.txt".format("Outputs/output_python_",filenumber)

with open(filename_output, "w") as file: 
    file.write(json.dumps(my_data))
file.close()
