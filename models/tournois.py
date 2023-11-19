

class Tournois:

    def __init__(self, nom, lieu, date_debut, date_fin, description, nbr_tour=4,liste_tour=[], liste_joueur=[]):
        """constructor"""
        self.nom = nom
        self.lieu = lieu
        self.date_debut = date_debut
        self.date_fin = date_fin
        self.list_tour = liste_tour
        self.list_joueur = liste_joueur
        self.description = description
        self.nbr_tour = nbr_tour


