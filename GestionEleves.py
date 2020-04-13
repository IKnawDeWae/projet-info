from lib_chargement_eleves import *
from lib_creation_eleve import *
from lib_supression_eleve import *

# Charge la liste des eleves au lancement du programme
eleves = charge_eleves()
# Boucle du menu principal
while True:
    print(eleves)
    print("1 - cree")
    print("2 - supprime")
    print("* - FIN")
    choix = input("choix:")
    if choix == "1":
        cree_eleve(eleves)
    if choix == "2":
        supprime_eleve(eleves)
    if choix == "*":
        break
