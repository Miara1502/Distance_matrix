file = pd.read_table('test_GE_Dist_Miara.tab')
head = file.head()
values = file.values

genes = file.index #Liste de tous les gènes
Y = values[:,0]  # => première colonne 0
X = values[:,0:2] # => 2 premières colonnes 1 et 2
test1 = file.index[values[:,0] > 10] # => renvoie la liste des gènes dont
#... la première colonne est supérieur
genes1 = values[0,:] #RENVOIE la première ligne
genes2 = values[1,:] # 2 em ligne
#Mettre 0 à la diagonale : Distance.loc['a']['b']

#Technique pour Créer la Matrice :
a = distance_all1(genes1)
b = distance_all1(genes2)
c = distance_all1(genes3)
Liste_Distance = []
Liste_Distance.append(a)
Liste_Distance.append(b)
Liste_Distance.append(c)

Matrice_Distance = pd.DataFrame(Liste_Distance)
#----------------------------------------------------------------------
#Autre Méthode pour créer une MAtrice de distance :
from scipy.spatial import distance_matrix
AB = distance_matrix([[5.86],[10.49] , [8.59]], [[5.38],[3.6],[6.7]])

#Plus simple :
#Pour Heure 1
A1 = values[:,0]
A1 = pd.DataFrame(A1)
MATRIX  = distance_matrix(A1,A1)



#Sélection des 10 gènes les plus proches
#exemple pour le gène 1 :
#Sort les résultats
M1 = Matrice_Distance['PF3D7_0100100']
M1 = M1.sort_values()
gene1_10 = M1[1:11]


M2 = Matrice_Distance[file.index[1]].sort_values()[1:11]
M3 = Matrice_Distance[file.index[2]].sort_values()[1:11].index # = gene1_100

dico1 = {}
dico[file.index[0]] = gene1_10.index

#MULTIPROCESSING

from multiprocessing import Pool
def f(x):
    return x*x

with Pool(5) as p :
    print(p.map(f,[1,2,3]))


multiprocessing.cpu_count()


#SYS :
import sys

print (len(sys.argv))
print ('Argument List:', str(sys.argv))


print ('Argument 1 :' , str(sys.argv[1])) # pour prendre le 2 em argument
