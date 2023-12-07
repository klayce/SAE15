import csv
import matplotlib.pyplot as plt #importation des bibliothèques
import numpy as np
#######################################Importation des fichiers csv############################################
data08=[]
with open('donnees_2008.csv',newline='') as csvfile:
    reader=csv.reader(csvfile,delimiter=',')
    for row in reader:
        data08.append(row)
#print(data08)

data16 = []
with open('donnees_2016.csv',newline='') as csvfile:
    reader=csv.reader(csvfile,delimiter=',')
    for row in reader:
        data16.append(row)
#print(data16)

data21 = []
with open('donnees_2021.csv',newline='') as csvfile:
    reader=csv.reader(csvfile,delimiter=';')
    for row in reader:
        data21.append(row)
#print(data21)

communes = []
with open('metadonnees_communes.csv',newline='') as csvfile:
    reader=csv.reader(csvfile,delimiter=';')
    for row in reader:
        communes.append(row)
        
##############################suppression la première ligne de chaque fichier csv################################
del data08[0]
del data16[0]
del data21[0]   
del communes[0]

#######################################Création des listes de la région l'Yonne############################################
reg89 = [] 
for i in range(len(data08)):
    data08[i][9] = int(data08[i][9])
    if data08[i][2] == '89': #89 est le code de la région l'Yonne
        reg89.append(data08[i])
#print(reg89)

#######################################Création des listes de la région l'Yonne 2016############################################
reg89_16 = []
for i in range(len(data16)):
    data16[i][9] = int(data16[i][9])
    if data16[i][2] == '89': 
        reg89_16.append(data16[i])
#print(reg89_16)

#######################################Création des listes de la région l'Yonne 2021############################################
reg89_21 = [] 
for i in range(len(data21)):
    data21[i][5] = int(data21[i][5])
    if data21[i][1] == '89':
        reg89_21.append(data21[i])
#print(reg89_21)

#######################################Calcul de la population de la région l'Yonne############################################
somme1 = sum(reg89[i][9] for i in range(len(reg89)))
somme2 = sum(reg89_16[i][9] for i in range(len(reg89_16)))
somme3 = sum(reg89_21[i][5] for i in range(len(reg89_21)))
print(somme1)
print(somme2)
print(somme3)

plt.plot([2008,2016,2021],[somme1,somme2,somme3])
plt.title('Evolution de la population de l\'Yonne')
plt.show()

#######################################Affichage du graphique############################################