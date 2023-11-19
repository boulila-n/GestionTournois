from models.joueur import Joueur


class ServiceJoueur:
    def __int__(self):
        pass

    def serialize_joueur(self, jr:Joueur):
        return {
        "prenom": jr.prenom,
        "nom": jr.nom,
        "date_naissance": jr.date_naissance
    }
