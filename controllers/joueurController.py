from views.joueurView import JoueurView
from views.menuView import MenuView
from models.joueur import Joueur
from tinydb import TinyDB

db = TinyDB("./database/db.json")
joueurs = db.table("joueurs")


class JoueurController:

    def __init__(self):
        """constructor"""
        self.joueurs = joueurs
        self.joueur_view = JoueurView()
        self.menu_view = MenuView()

    def sauvegarderJoueur(self, jr: Joueur):
        self.joueurs.insert(jr.serialize_joueur)

    def get_joueur_infos(self, prenom=None, nom=None):
        if (prenom and nom) is None:
            prenom = self.menu_view.get_input(self, "le prénom", "joueur")
            nom = self.menu_view.get_input(self,"le nom", "joueur")
            date_naissance = self.menu_view.get_input(self, "la date de naissance", "joueur")
            joueur_1 = Joueur(nom, prenom, date_naissance)
            self.sauvegarderJoueur(joueur_1)
            print(f"{nom} {prenom} a bien été ajouté à la base de données")

    def print_infos(self, jr):
        self.joueur_view.print_jr_infos(
            jr.doc_id,
            jr["prenom"],
            jr["nom"],
            jr["date_naissance"])

    def get_table(self):
        if self.joueurs:
            self.joueur_view.print_titles()
            for j in self.joueurs:
                self.print_infos(j)
            return self.joueurs