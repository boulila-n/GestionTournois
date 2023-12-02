from services.servicetournois import ServiceTournois
from views.menuView import MenuView
from models.tournois import Tournois
from views.tournoisView import TournoisView
from controllers.joueurController import JoueurController
from tinydb import TinyDB


db = TinyDB("./database/db.json")
tournois = db.table("tournois")


class TournoisContoller:

    def __init__(self):
        """constructor"""
        self.tournois = tournois
        self.tournois_view = TournoisView()
        self.menu_view = MenuView()
        self.service_tournois = ServiceTournois()
        self.joueur_controller = JoueurController()

    def creer_tournois(self):
        nbr_turn_default = 4
        name = self.tournois_view.get_string_value("le nom", "tournoi")
        location = self.tournois_view.get_string_value("la localisation", "tournoi")
        start_date = self.tournois_view.get_string_value("la date du début", "tournoi")
        end_date = self.tournois_view.get_string_value("la date de fin", "tournoi")
        description = self.tournois_view.get_string_value("la description", "tournoi")
        number_of_turn = int(self.tournois_view.get_string_value("le nombre", f"tours ou laisser vide ({nbr_turn_default} par défaut)"))
        nbr_jr =int(self.tournois_view.get_string_value("le nombre", "joueurs"))

        tournament = Tournois(name, location, start_date, end_date, description,[], nbr_jr, number_of_turn)
        new_id = self.sauvegarderTournois(tournament)
        print(f"Le tournoi {tournament.nom} a été crée avec succès")
        return self.get_tournoi_id(new_id)

    def afficher_liste_tournois(self):
        if self.tournois:
            self.tournois_view.print_titles()
            for tr in self.tournois:
                self.print_infos(tr)
            return self.tournois.__len__()

    def selectioner_tournoi(self):
        value = input(f"Veuillez saisir l'id tournoi choisi : ")
        if not value:
            print("Votre saisie n'a pas été comprise")
            print(
                f"veuillez rééssayer d'indiquer l'id de tournoi"
            )
        else:
            return value

    def print_infos(self, tr):
        self.tournois_view.afficher_tournement(
            tr.doc_id,
            tr["nom"],
            tr["lieu"],
            tr["date_debut"],
            tr["date_fin"],
            tr["description"],
            tr["nbr_jr"])

    def sauvegarderTournois(self, tr: Tournois):
        return self.tournois.insert(self.service_tournois.serialize_tournois(tr))

    def get_tournoi_id(self, id: int):
        tournoi = self.tournois.get(doc_id=int(id))
        if tournoi:
            return tournoi
        return None

    def update_tournoi(self,tournoi):
        self.tournois.update(
            self.service_tournois.serialize_tournois(tournoi), doc_ids=[tournoi.id])

    def random_matchs(self, tr):
        pairs = []
        liste_jr = tr["list_joueur"]
        nbr = tr["nbr_jr"]
        jr1 = liste_jr[0: int(nbr / 2)]
        jr2 = liste_jr[int(nbr / 2):]
        for index in range(int(nbr / 2)):
            pair = [jr1[index], jr2[index]]
            pairs.append(pair)
        return pairs

    def afficher_jr(self, jr):
        return jr["nom"] + " " + jr["prenom"]

    def start_match(self, m):
        nom_j1 = self.afficher_jr(m[0])
        nom_j2 = self.afficher_jr(m[1])
        print("MATCH :")
        print(nom_j1 + " VS " + nom_j2)

