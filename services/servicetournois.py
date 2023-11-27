from models.tournois import Tournois
from services.servicejoueur import ServiceJoueur

class ServiceTournois:

    def __int__(self):
        self.service_jr = ServiceJoueur

    def serialize_tournois(self, tr: Tournois):
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

    def deserialize_tournois(self, tr):
        tournoi = Tournois(
            tr["nom"],
            tr["lieu"],
            tr["date_debut"],
            tr["date_fin"],
            tr["description"],
            tr["list_joueur"],
            tr["nbr_jr"],
            tr["nbr_tour"])
        tournoi.id = tr.doc_id
        return tournoi