# author:ismailguzel

import sys

dimmatrix = int(sys.argv[1])
homclass = int(sys.argv[2])
epsilonstart = int(sys.argv[3])
epsilonend = float(sys.argv[4])
epsilonstep = float(sys.argv[5])

import json
with open("Outputs/simplex_with_epsilon.txt", "r") as file:
    res=json.loads(file.read())

def myfunc(eps,res):
    return [e[0] for e in res if(e[1]<=eps)]


def mymatrix(dimmatrix, n, epsilon1, epsilon2):    
    X1=SimplicialComplex(myfunc(epsilon1,res))   
    X2=SimplicialComplex(myfunc(epsilon2,res))
    X1.set_immutable()
    X2.set_immutable()
    CC1 = X1.n_chains(2, QQ).chain_complex()
    CC2 = X2.n_chains(2, QQ).chain_complex()
    HX1=X1.homology_with_basis(QQ)
    HX1_basis = HX1.basis()
    mylast = []
    for i in range(CC1.betti(n)):
        for j in range(i+1,CC1.betti(n)):
            diff = HX1_basis[n,i].to_cycle()-HX1_basis[n,j].to_cycle()
            if diff==0:
                break
            mylist = list(diff.to_vector())
            mydim = CC1.differential(1).dimensions()
            mydim1 =CC2.differential(1).dimensions()
            for i in range(mydim1[0]-mydim[0]):
                mylist.append(0)
            mytuple= tuple(mylist)
            myoriginal = CC2.differential(1)
            mylist = list(CC2.differential(1).transpose())
            mylist.append(mytuple)
            mylist = [list(tp) for tp in mylist]
            if rank(myoriginal)==rank(matrix(mylist)):
                  mylast.append([HX1_basis[0,i].to_cycle(),HX1_basis[0,j].to_cycle()]) 
    import re
    import numpy as np
    rows = [ int(re.findall(r"\d+", str(index[0]) )[0]) for index in mylast]
    columns = [ int(re.findall(r"\d+", str(index[1]) )[0]) for index in mylast]
    A = 10*np.ones((dimmatrix,dimmatrix))
    for i in range(len(rows)):
        A[rows[i]][columns[i]] = epsilon2
        A[columns[i]][rows[i]] = epsilon2
    return A


def distancematrix(dimmatrix, n, eps1, eps2, step):
    import numpy as np
    epsilon1 = np.arange(eps1, eps2, step)
    epsilon2 = np.arange(eps1+step , eps2+step, step)
    A = []
    for i in range(len(epsilon1)):
        A.append(mymatrix(dimmatrix, n, epsilon1[i], epsilon2[i]))
    B = A[0]
    for i in range(len(epsilon1)-1):
        B = np.where(B <= A[i+1], B, A[i+1])
    return B

C = distancematrix(dimmatrix, homclass, epsilonstart, epsilonend, epsilonstep)

import pandas as pd
dataframe = pd.DataFrame(C)
dataframe.to_csv("Outputs/homological_distance.txt")
