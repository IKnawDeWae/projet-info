def display():
	file = open("Ordi1.csv", "r")
	liste = []
	a = int(input("choisissez un ordinateur :"))
	for ligne in file:
		champs = ligne.split(";")
		liste.append(champs)
		#ecrire description pour les prints exemple ligne 7
	print(liste[a][0])
	print(liste[a][1])
	print(liste[a][2])
	print(liste[a][3])
	print(liste[a][4])
	print(liste[a][5])
	print(liste[a][6])
	print(liste[a][7])
	print(liste[a][8])
	print(liste[a][9])
	print(liste[a][10])
	print(liste[a][11])
	print(liste[a][12])
	print(liste[a][13])
	print(liste[a][14])
	print(liste[a][15])


	#print(liste[a][16])
def displayAll():
	file = open("Ordi1.csv", "r")
	liste = []
	for ligne in file:
		champs = ligne.split(";")
		liste.append(champs)
	print(liste)


	#cette fonction affiche tous les ordinateurs
def displayDate():
	x = 0
	file = open("Ordi1.csv", "r")
	liste = []
	for ligne in file:
		champs = ligne.split(";")
		liste.append(champs)
	while x < 10:
		x = x + 1
		print(liste[x][0], liste[x][13], liste[x][14], liste[x][15])
	#ca cest les requete Gutave tu dois modifier le fichier csv pour que ca marche bien
