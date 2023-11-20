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

    def create_tournois(self):
        nbr_turn_default = 4
        name = self.tournois_view.get_string_value("le nom", "tournoi")
        location = self.tournois_view.get_string_value("la localisation", "tournoi")
        start_date = self.tournois_view.get_string_value("la date du début", "tournoi")
        end_date = self.tournois_view.get_string_value("la date de fin", "tournoi")
        description = self.tournois_view.get_string_value("la description", "tournoi")
        number_of_turn = self.tournois_view.get_string_value("le nombre", f"tours ou laisser vide ({nbr_turn_default} par défaut)")
        nbr_jr =int(self.tournois_view.get_string_value("le nombre", "joueurs"))
        list_joueur =[]
        for i in range(nbr_jr):
            print("ajouter le joueur numéro: ", i+1)
            jr = self.joueur_controller.get_joueur_infos()
            list_joueur.append(jr)
        tournament = Tournois(name, location, start_date, end_date, description,nbr_jr, list_joueur, number_of_turn)
        self.sauvegarderTournois(tournament)
        print (f"Le tournoi {tournament.nom} a été crée avec succès")



    def sauvegarderTournois(self, tr: Tournois):
        self.tournois.insert(self.service_tournois.serialize_tournois(tr))
