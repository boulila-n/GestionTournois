class Tournois:

    def __init__(self, nom, lieu, date_debut, date_fin, numero, liste_tour, liste_joueur, description, nbr_tour=4):
        """constructor"""
        self.nom = nom
        self.lieu = lieu
        self.date_debut = date_debut
        self.date_fin = date_fin
        self.numero = numero
        self.list_tour = []
        self.list_joueur = []
        self.description = description
        self.nbr_tour = nbr_tour

