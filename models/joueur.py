class Joueur:

    def __init__(self, nom, prenom, date_naissance):
        """constructor"""
        self.nom = nom
        self.prenom = prenom
        self.date_naissance = date_naissance

    @property
    def serialize_joueur(self):
        return {
            "prenom": self.prenom,
            "nom": self.nom,
            "date_naissance": self.date_naissance
        }