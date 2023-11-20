from models.tournois import Tournois


class ServiceTournois:

    def __int__(self):
        pass

    def serialize_tournois(self, tr: Tournois):
        '''Returns the dictionary of class attributes.

        '''
        return {
            "nom": tr.nom,
            "lieu": tr.lieu,
            "date_debut": tr.date_debut,
            "date_fin": tr.date_fin,
            "description": tr.description,
            "list_joueur": tr.list_joueur,
            "nbr_jr": tr.nbr_jr,
            "nbr_tour": tr.nbr_tour
        }