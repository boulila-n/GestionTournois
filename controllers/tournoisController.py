from services.servicetournois import ServiceTournois
from models.tournoi import Tournoi
from models.match import Match
from models.tour import Tour
from views.tournoisView import TournoisView
from controllers.joueurController import JoueurController
from tinydb import TinyDB
from tinydb import Query
from datetime import datetime


db = TinyDB("./database/db.json")
tournois = db.table("tournois")


class TournoisContoller:

    def __init__(self):
        """constructor"""
        self.tournois = tournois
        self.tournois_view = TournoisView()
        self.service_tournois = ServiceTournois()
        self.joueur_controller = JoueurController()

    def creer_tournois(self):
        nbr_turn_default = 4
        name = self.tournois_view.get_string_value("le nom", "tournoi")
        location = self.tournois_view.get_string_value("la localisation",
                                                       "tournoi")
        start_date = self.tournois_view.get_date(self, "la date du début",
                                             "tournoi")
        end_date = self.tournois_view.get_date(self, "la date de fin",
                                           "tournoi")
        description = self.tournois_view.get_string_value("la description",
                                                          "tournoi")
        number_of_turn = (self.tournois_view
                          .get_default_value("le nombre",
                                             f"tours "
                                             f"ou laisser vide"
                                             f"({nbr_turn_default}"
                                             f" par défaut)"))
        if number_of_turn:
            number_of_turn = int(number_of_turn)
        else:
            number_of_turn = nbr_turn_default
        nbr_jr = 0
        while nbr_jr < 2 or nbr_jr % 2 != 0:
            nbr_jr = (self.tournois_view
                      .get_string_value("le nombre",
                                        "joueurs "
                                        "(* nombre pair "
                                        "au moins égal à deux *)"))
            if nbr_jr:
                nbr_jr = int(nbr_jr)

        tournament = Tournoi(name, location, start_date,
                             end_date, description, nbr_jr, number_of_turn)
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
        value = input(f'{"Veuillez saisir l id tournoi choisi : "}')
        if not value:
            print("Votre saisie n'a pas été comprise")
            print(f'{"veuillez réessayer d indiquer l id de tournoi"}')
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

    def sauvegarderTournois(self, tr: Tournoi):
        return self.tournois.insert(self
                                    .service_tournois.serialize_tournois(tr))

    def get_tournoi_id(self, id: int):
        tournoi = self.tournois.get(doc_id=int(id))
        if tournoi:
            return tournoi
        return None

    def update_tournoi(self, tournoi):
        self.tournois.update(
            self.service_tournois.serialize_tournois(tournoi),
            doc_ids=[tournoi.id])

    def random_matchs(self, tr):
        pairs = []
        liste_jr = sorted(tr["list_joueur"],
                          key=lambda jr: (jr["points"]), reverse=True)
        while liste_jr:
            index = 1
            while (index <= len(liste_jr) and len(liste_jr) > 2
                   and liste_jr[index]["id"] in liste_jr[0]["opposants"]):
                index += 1
            pair = [liste_jr[0], liste_jr[index]]
            liste_jr[0]["opposants"].append(liste_jr[index]["id"])
            liste_jr[index]["opposants"].append(liste_jr[0]["id"])
            del liste_jr[index]
            del liste_jr[0]
            pairs.append(pair)
        return pairs

    def getNameJr(self, jr):
        return jr["nom"] + " " + jr["prenom"]

    def convertir_to_match(self, m):
        nom_j1 = self.getNameJr(m[0])
        nom_j2 = self.getNameJr(m[1])
        match = Match(nom_j1, nom_j2)
        return match

    def creer_tour(self, tr, nbr):
        name = "Round" + str(nbr)
        tournoi = self.service_tournois.deserialize_tournois(tr)
        created_at = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        matchs = self.generer_matchs(tr)
        round = Tour(name, str(created_at), matchs)
        tours = self.get_tr_tours(tr)
        db_round = self.entrer_resultats_matchs(
            self.service_tournois.serialize_tour(round), tr)
        self.update_tours(tours, tournoi, db_round)
        return self.get_tournoi_id(tr.doc_id)

    def update_tours(self, tours, tournoi, round):
        tours.append(round)
        tournoi.tours = tours
        self.update_tournoi(tournoi)
        return round

    def get_tr_tours(self, tr):
        tournoi = self.tournois.get(doc_id=int(tr.doc_id))
        if tournoi:
            return tournoi["tours"]
        return None

    def generer_matchs(self, tr):
        matchs = self.random_matchs(tr)
        list_matchs = []
        if matchs:
            for m in matchs:
                list_matchs.append(self.convertir_to_match(m))
        return list_matchs

    def entrer_resultats_matchs(self, tour, tr):
        if tour and tour["matchs"]:
            for m in tour["matchs"]:
                self.set_match_result(m)
                self.set_points_jr(tr, m["joueur_1"], m["score_joueur_1"])
                self.set_points_jr(tr, m["joueur_2"], m["score_joueur_2"])
            tour["termine"] = True
            tour["date_fin"] = str(datetime.now()
                                   .strftime("%Y-%m-%d %H:%M:%S"))
            return tour
        else:
            print(" *** Veuillez réssayer votre choix ***")

    def set_match_result(self, match):
        print("MATCH " + match["joueur_1"] + " vs " + match["joueur_2"])
        match_null = self.si_match_null()

        if match_null == "Y":
            match["score_joueur_1"] = 0.5
            match["score_joueur_2"] = 0.5
        else:
            jr1 = self.si_jr1_gagne(match["joueur_1"])
            if jr1 == "Y":
                match["score_joueur_1"] = 1
                match["score_joueur_2"] = 0
            else:
                match["score_joueur_1"] = 0
                match["score_joueur_2"] = 1

    def set_points_jr(self, tr, jr, score):
        list_jr = tr["list_joueur"]
        for j in list_jr:
            if (j["nom"] + " " + j["prenom"]) == jr:
                j["points"] = j["points"] + score

    @staticmethod
    def tour_en_cours(tours):
        for t in tours:
            if not t["termine"] and t["date_fin"] is None:
                return t
        return None

    @staticmethod
    def si_jr1_gagne(jr):
        rep = None
        while rep is None or rep.upper() not in ["Y", "N"]:
            rep = input(f'{"Le joueur " + jr + "a gagné ou non ? (Y/N): "}')
        return rep.upper()

    @staticmethod
    def si_match_null():
        rep = None
        while rep is None or rep.upper() not in ["Y", "N"]:
            rep = input(f'{"Le match est null ? (Y par défaut/N): "}')
        return rep.upper()

    @staticmethod
    def get_confirmation():
        confirm = ""
        while confirm not in ["Y", "N"]:
            confirm = input("Confirmez-vous ? (Y/N): ").upper()
            if confirm not in ["Y", "N"]:
                print(
                    "Veuillez saisir à nouveau s'il vous plaît."
                )
            return confirm

    def get_sorted_joueurs(self, tr):
        list = sorted(tr["list_joueur"],
                      key=lambda jr: (jr["nom"], jr["prenom"]))
        self.tournois_view.print_titles_jr()
        for j in list:
            self.print_infos_jr(j)

    def print_infos_jr(self, jr):
        self.tournois_view.print_jr_infos(
            jr["nom"],
            jr["prenom"],
            jr["date_naissance"],
            jr["points"])

    def print_infos_tour(self, t):
        self.tournois_view.print_tour_infos(
            t["nom"])

    def print_infos_match(self, m, i):
        self.tournois_view.print_match_infos(
            i,
            m["joueur_1"],
            m["score_joueur_1"],
            m["joueur_2"],
            m["score_joueur_2"])

    def sort_joueur_score(self, tr):
        list = sorted(tr["list_joueur"],
                      key=lambda jr: (jr["points"]), reverse=True)
        self.tournois_view.print_titles_jr()
        for j in list:
            self.print_infos_jr(j)

    def get_tous_tours(self, tr):
        list = sorted(tr["tours"], key=lambda t: (t["nom"]))
        if list:
            self.tournois_view.print_titles_tour()
            for t in list:
                matchs = t["matchs"]
                self.print_infos_tour(t)
                i = 1
                for m in matchs:
                    self.print_infos_match(m, i)
                    i = i + 1

    def get_tournoi_nom(self):
        Tournoi = Query()
        str = self.tournois_view.get_string_value("Le nom",
                                                  " Tournoi à chercher ")
        tournoi = self.tournois.get(Tournoi.nom == str)
        if tournoi:
            print(f'{"=" * 75}')
            print("Tournoi : " + tournoi["nom"] + " Début : "
                  + tournoi["date_debut"]
                  + " Fin le : " + tournoi["date_fin"])
            print(f'{"=" * 75}')
        else:
            print("Impossible de trouver le tournoi.")
