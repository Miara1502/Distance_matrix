import pandas as pd
import numpy as np
import scipy
import multiprocessing

file = pd.read_table('test_GE_Dist_Miara.tab')
values = file.values

#Distance entre 2 genes
def distance_2genes(gene_A , gene_B ) :
    sum = 0
    dist = 0  ; dist = [] ; sum = 0
    for i in range(len(file.columns)) :
        diff = abs(gene_A[i] - gene_B[i])
        sum = sum + diff
    return sum

#Distance entre genes1 et tous les autres (100 genes)
nb_gene = len(file.index)
liste_dist_geneA = []

def distance_all1(genesA ):
    liste_dist_gene1 = []
    for i in range(nb_gene) :
        genesB = values[i , :]
        y = distance_2genes(genesA , genesB)
        liste_dist_gene1.append(y)
    return liste_dist_gene1

def liste_distance(file) :
    matrice = []
    for i in range(nb_gene) :
        matrice.append(distance_all1(file.values[i,:]))
    return matrice

Matrice_Distance = liste_distance(file)
Matrice_Distance = pd.DataFrame(Matrice_Distance)
#-------------------------------------------------------------------------------
#TRAITEMENT MATRICE DE DISTANCE :
#Mettre le nom de gènes comme indice
for i in range(len(file.index)) :
    Matrice_Distance= Matrice_Distance.rename(index= {i:file.index[i]})
    Matrice_Distance= Matrice_Distance.rename(columns= {i:file.index[i]})

'''def dico_matrice(matrice, N):
    dico = {}
    for i in range(len(matrice)):
        dico[file.index[i]] =  matrice[file.index[i]].sort_values()[1:N].index
    return dico;'''

def dico_matrice(matrice):
    dico = {}
    for i in range(len(matrice)):
        dico[file.index[i]] =  matrice[file.index[i]].sort_values()[1:10].index
    return dico;

#MULTIPROCESSING
from multiprocessing import Pool
with Pool(5) as p :
    print(p.map(dico_matrice,[Matrice_Distance]))

#OUTPUT
print('\n')
DICO = dico_matrice(Matrice_Distance)
''''DICO = dico_matrice(Matrice_Distance,10)'''
#exemple
print('Exemple du gene le plus proche de PFD37_0101200:')
print(DICO['PF3D7_0101200'][0])
print('\n')
#Nombre de processeur utiliser :
print("le nombre de processeur utilisé est de {}".format(multiprocessing.cpu_count()))
