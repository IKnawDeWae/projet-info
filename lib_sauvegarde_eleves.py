def sauve_eleves(liste):
    acces_fichier = open("eleves.csv", "w")
    for eleve in liste:
        acces_fichier.write(str(eleve[0]))
        acces_fichier.write(";")
        acces_fichier.write(eleve[1])
        acces_fichier.write(";")
        acces_fichier.write(eleve[2])
        acces_fichier.write(";")
        acces_fichier.write(eleve[3])
        acces_fichier.write("\n")
    acces_fichier.close()

# Test unitaire
#from lib_chargement_eleves import *
#test = charge_eleves()
#print(test)
#from lib_creation_eleve import *
#cree_eleve(test)
#print(test)
#sauve_eleves(test)
