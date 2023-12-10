from models.tournoi import Tournoi
from models.tour import Tour
from models.match import Match
from services.servicejoueur import ServiceJoueur


class ServiceTournois:

    def __int__(self):
        self.service_jr = ServiceJoueur

    def serialize_tournois(self, tr: Tournoi):
        return {
            "nom": tr.nom,
            "lieu": tr.lieu,
            "date_debut": tr.date_debut,
            "date_fin": tr.date_fin,
            "description": tr.description,
            "list_joueur": tr.list_joueur,
            "tours": tr.tours,
            "nbr_jr": tr.nbr_jr,
            "nbr_tour": tr.nbr_tour
        }

    def deserialize_tournois(self, tr):
        tournoi = (
            Tournoi(
                tr["nom"],
                tr["lieu"],
                tr["date_debut"],
                tr["date_fin"],
                tr["description"],
                tr["nbr_jr"],
                tr["nbr_tour"],
                tr["list_joueur"],
                tr["tours"]))
        tournoi.id = tr.doc_id
        return tournoi

    def serialize_tour(self, tr: Tour):
        return {
            "nom": tr.nom,
            "date_debut": tr.date_debut,
            "date_fin": tr.date_fin,
            "termine": tr.termine,
            "matchs": self.serialize_liste_match(tr.matchs)
        }

    def serialize_match(self, m: Match):
        return {
            "joueur_1": m.joueur_1,
            "joueur_2": m.joueur_2,
            "score_joueur_1": m.score_joueur_1,
            "score_joueur_2": m.score_joueur_2
        }

    def serialize_liste_match(self, liste):
        return [self.serialize_match(m) for m in liste]
