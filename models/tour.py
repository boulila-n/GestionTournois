class Tour:

    def __init__(self, nom, date_debut, date_fin, termine=True):
        """constructor"""
        self.matchs = []
        self.nom = nom
        self.date_debut = date_debut
        self.date_fin = date_fin
        self.termine = termine