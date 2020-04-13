from Afficher import*

def deletePc():
    file = open("Ordi1.csv","w")
    liste = []
    for equipement in liste:
        print("ordinateur:",[0],"-element:",element[1])
    # Choix de l'eleve a supprimer
    choix = int(input("id a supprimer:"))
    # Attention: on passe par l'index de liste pour pouvoir faire la suppression
    for i in range(0,len(liste)):
        if liste[i][0] == choix:
            del(liste[i])
            # Attention, il faut absolument le "break" car, sinon, la boucle
            # continue apres le "del" comme si de rien etait mais, comme la
            # liste est plus courte, la boucle "plante" sur le dernier element
            # car celui-ci n'existe plus !
            break

