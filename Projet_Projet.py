import csv
from function import *       

liste = []

with open (r"Projet/Mine.csv") as f:   
    fichierCsv = csv.reader(f)

    for row in fichierCsv:
        if row[2] != "" and row[3] != "":
            liste.append(row)

invalide = [liste[0]]
# print(invalide)
valide = [liste[0]]

 # suppression du premier element de chaque ligne
for elem in liste:
    del elem[0:1]

for i in range(1, len(liste)):
    # print(data[i][0])

    if liste[i][5] != "":
        liste[i][5] = note_verification(liste[i][5])
    if liste[i][3] != "":        
        liste[i][3] = date(liste[i][3])
        # print(data[i][3])

    if num(liste[i][0]) and verify_date(liste[i][3]) and classe(liste[i][4]):
        if type(liste[i][5]) == str :
            invalide.append(liste[i])
        else:
            vide = []
            p = 0
            for elem in liste[i][5].values():
                vide.extend(elem)
            for elem in liste[i][5].values():
                vide.extend(elem)
            for s in vide:
                if verf(s):
                    p = p + 1
            if p >= 1:
                invalide.append(liste[i])
            else:
                valide.append(liste[i])
    else:
        invalide.append(liste[i])
        # print(invalide)

# Données valide dans un fichier nommé Donnée_valide

Donnée_valide = valide.copy()
Donnée_valide
# print(Donnée_valide)

key = [k for k in Donnée_valide[0]]
key
# print(key)
# Valeurs dictionnaire

value = []

for i in range (6):
    d = []
    j = 1
    while j < len(Donnée_valide):
        # print(Donnée_valide[j][i])
        d.append(Donnée_valide[j][i])
        j += 1
    value.append(d)
# print(value)

# Le menu de la plateforme :
# créer un menu permettant


liste = Donnée_valide
liste1 = invalide
listes = Donnée_valide + invalide
# print(liste)
def chercher(b):
    b = input("Entrer le numero de l'élève :")
    for i in listes:
        if i[0] == b:
            print(i)

def meilleur(moy):
    s = 0
    for k in listes:
        pass
#  D’afficher les informations (Valide ou invalide ; au choix)
print("Bienvenue dans SAMA SCOOL")
a =input("1-afficher les informations (Valide)\n2-afficher les informations Invalides\n3-Chercher les informations (élève)\n")

if a == "1": print("les données valides sont\n",Donnée_valide)
if a == "2": print("les données invalide sont\n",invalide)
if a == "3": 
    # print("Entrer le numéro de l'élève ")
    #  D’afficher une information (par son numéro)

    b = input("loading ...")
    if chercher(b):
        print("C'est le numero :", b)
    else: 
        print("Le numéro n'est pas dans la base")

#  D’afficher les cinq premiers
#  De modifier une information invalide ensuite le transférer dans la structure où se
# trouve les informations valides

