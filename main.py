from Afficher import *
from creer_ordi import *
#from supression_element import *
from Delete1 import*

print("c → créer un ordi/logiciel")
print("a → Aficcher tous les equipement/logiciel")
print("m → Modifier un équipement/logiciel")
print("s → Supprimer un équipement/logiciel")
print("r → Choisir un requète/logiciel")

choix = input("votre choix: ")

if choix == "c":
	creer_ordi()
if choix == "a":
	print("x → Afficher tous les ordinateurs")
	print("o → Afficher un seul ordinateur")
	choix2 = input("Que désirez-vous?:")
	if choix2 == "x":
		displayAll()
	if choix2 == "o":
		display()
if choix == "m":
	modif - equip()
if choix == "s":
	deletePc()
if choix == "r":
	displayDate()
#print("d → Date d'achat")
#print("q → Date d'expiration")
#print("v → version de système")
#a c'est bon
#r c'est bon
