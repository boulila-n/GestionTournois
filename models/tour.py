class Tour:

    def __init__(self, nom, date_debut, matchs, date_fin=None,
                 termine=False):
        """constructor"""
        self.matchs = matchs
        self.nom = nom
        self.date_debut = date_debut
        self.date_fin = date_fin
        self.termine = termine
