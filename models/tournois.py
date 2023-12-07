from models.joueur import Joueur


class Tournois:

    def __init__(self, nom, lieu, date_debut, date_fin, description, nbr_jr, nbr_tour=4, list_joueur=[], tours = []):
        """constructor"""
        self.nom = nom
        self.lieu = lieu
        self.date_debut = date_debut
        self.date_fin = date_fin
        self.description = description
        self.nbr_jr = nbr_jr
        self.list_joueur = list_joueur
        self.tours = tours
        self.nbr_tour = nbr_tour



