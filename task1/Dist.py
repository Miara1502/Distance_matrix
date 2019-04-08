import pandas as pd
import numpy as np
import scipy

file = pd.read_table('test_GE_Dist_Miara.tab')
values = file.values
genes1 = values[0,:] #RENVOIE la première ligne
genes2 = values[1,:] # 2 em ligne
genes3 = values[2,:]

taille = len(file.columns)

#Distance entre 2 genes
def distance_2genes(gene_A , gene_B , taille) :
    sum = 0
    dist = 0  ; dist = [] ; sum = 0
    for i in range(taille) :
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
        y = distance_2genes(genesA , genesB , taille)
        #print(y)
        liste_dist_gene1.append(y)
    return liste_dist_gene1

def liste_distance(file) :
    matrice = []
    for i in range(nb_gene) :
        matrice.append(distance_all1(file.values[i,:]))
    return matrice

Matrice_Distance = liste_distance(file)
Matrice_Distance = pd.DataFrame(Matrice_Distance)

#Mettre le nom de gènes comme indice
for i in range(len(file.index)) :
    Matrice_Distance= Matrice_Distance.rename(index= {i:file.index[i]})
    Matrice_Distance= Matrice_Distance.rename(columns= {i:file.index[i]})

#Mettre dans un dictionnaire :
dico = {}
for i in range(len(file.index)) :
    dico[file.index[i]] =  Matrice_Distance[file.index[i]].sort_values()[1:11].index ;


print(dico)
print('\n')
print('le plus proche du gène est {}'.format(dico['PF3D7_0104900'][0]))
