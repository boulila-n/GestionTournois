class Joueur:

    def __init__(self, nom, prenom, date_naissance, rang = 0, points = 0, id = None, opposants = []):
        """constructor"""
        self.nom = nom
        self.prenom = prenom
        self.date_naissance = date_naissance
        self.rang = rang
        self.points = points
        self.id = id
        self.opposants = opposants