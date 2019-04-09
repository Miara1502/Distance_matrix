#!/usr/bin/python
#python3 Dist_multi.py test_GE_Dist_Miara.tab

import pandas as pd
import numpy as np
import scipy
import multiprocessing
import math

dt = pd.read_csv('1000genes', sep = '\t')
#dt = pd.read_csv('test_GE_Dist_Miara.tab', sep = '\t')

#Distance MATRIX
from scipy.spatial import distance_matrix
ndarray = scipy.spatial.distance.pdist(dt)

matrix_uni = scipy.spatial.distance.squareform(ndarray)
matrix = pd.DataFrame(matrix_uni)

#matrix.shape[0] => dimension matrice
for i in range(len(matrix)) :
    matrix= matrix.rename(index= {i:dt.index[i]})
    matrix= matrix.rename(columns= {i:dt.index[i]});

#Création dictionnaire :
def dico_matrice(matrice):
    dico = {}
    for i in range(len(matrice)):
        #dico[dt.index[i]] =  matrice[dt.index[i]].sort_values()[1:10].index
        dico[dt.index[i]] =   matrice[dt.index[i]].sort_values()[1:11]
    return dico;

from multiprocessing import Pool
with Pool(5) as p :
    print(p.map(dico_matrice,[matrix]))

#DICO = dico_matrice(matrix)

multiprocessing.cpu_count()

