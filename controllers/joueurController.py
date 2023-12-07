from views.joueurView import JoueurView
from views.menuView import MenuView
from models.joueur import Joueur
from tinydb import TinyDB
from services.servicejoueur import ServiceJoueur
from datetime import datetime

db = TinyDB("./database/db.json")
joueurs = db.table("joueurs")


class JoueurController:

    def __init__(self):
        """constructor"""
        self.joueurs = joueurs
        self.joueur_view = JoueurView()
        self.menu_view = MenuView()
        self.service_joueur = ServiceJoueur()

    def sauvegarderJoueur(self, jr: Joueur):
        return self.joueurs.insert(self.service_joueur.serialize_joueur(jr))

    def modifier(self):
            prenom = self.menu_view.get_input(self, "le prénom", "joueur à modifier")
            nom = self.menu_view.get_input(self, "le nom", "joueur à modifier")
            result = None
            for jr in self.joueurs:
                if jr["prenom"] == prenom and jr["nom"] == nom:
                    print("Le joueur est trouvé ")
                    result = jr
            if result:
                self.saisie_modif(result)
            else:
                print("Joueur non trouvé ")

    def saisie_modif(self, jr):
        prenom1 = self.menu_view.get_input(self, "le nouveau prénom", "joueur")
        nom1 = self.menu_view.get_input(self, "le nouveau nom", "joueur")
        date_naiss = self.menu_view.get_input(self, "la nouvelle date de naissance", "joueur")
        modif = Joueur(nom1, prenom1, date_naiss)
        self.update_joueur(modif, jr.doc_id)
        print("Modification avec succés !")

    def update_joueur(self, joueur: Joueur, jr_id: int):
        self.joueurs.update(self.service_joueur.serialize_joueur(joueur), doc_ids=[int(jr_id)])

    def get_joueur_infos(self):
            prenom = self.menu_view.get_input(self, "le prénom", "joueur")
            nom = self.menu_view.get_input(self,"le nom", "joueur")
            date_naissance = self.menu_view.get_date(self,"la date de naissance", "joueur")
            joueur_1 = Joueur(nom, prenom, date_naissance)
            id = self.sauvegarderJoueur(joueur_1)
            print(f"{nom} {prenom} a bien été ajouté à la base de données")
            return id

    def get_joueur_id(self, id: int):
        jr = self.joueurs.get(doc_id=int(id))
        if jr:
            return jr
        return None

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