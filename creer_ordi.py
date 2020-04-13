from Afficher import*
def creer_ordi():
	# Determine un identifiant unique
	liste=[]
	numero_ordi = 0
	for Ordi1 in liste:
		if Ordi1[0] >= numero_ordi:
			numero_ordi = Ordi1[0] + 1
	# Saisie des autres informations
	Processeur = input("Processeur:")
	RAM = input("RAM:")
	Type_bus = input("Type de bus:")
	C_G = input("Carte graphique:")
	Port_Video = input("port vidéo:")
	Résolution = input("Résolution de l'écran:")
	Taille = input("Taille de l'écran:")
	Nombre_ports_USB = input("Nombre de ports USB:")
	Stockage = input("Stockage:")
	Lecteur = input("Lecteur/graveur de CD:")
	Carte_Réseau = input("Carte réseau:")
	Wifi = input("WiFi:")
	Blt = input("Bluetooth:")
	# Ajout de la sous-liste des nouvelles donnees en fin de la liste des ordinateurs
	liste.append([
	    numero_ordi, Processeur, RAM, Type_bus, C_G, Port_Video, Résolution,
	    Taille, Nombre_ports_USB, Stockage, Lecteur, Carte_Réseau, Wifi, Blt
	])
