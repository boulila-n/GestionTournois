
from abc import ABC
from services.serviceutils import (is_valid_date, datetime_to_str)


class MenuView(ABC):

    @staticmethod
    def print_menu():
        print(f'{"=" * 119}')
        print(f'{"* MENU PRINCIPAL*"}'.center(119))
        print("1. Ajouter un nouveau joueur")
        print("2. Afficher la liste des joueurs par ordre alphabétique")
        print("3. Modifier joueur")
        print("4. Créer un nouveau tournois")
        print("5. Reprendre un tournois")
        print("6. Afficher la liste de tous les tournois")
        print("7. Rechercher un tournois")
        print("0. Quitter le programme")
        print(f'{"=" * 119}')

    def nbr_jr_ajoutes(self, tr):
        return str(len(tr["list_joueur"])) + "/" + str(tr["nbr_jr"])

    def print_menu_tournois(self, tournoi):
        nbr_jrs = len(tournoi["list_joueur"])
        nbr_tours = len(tournoi["tours"])
        max_tour = tournoi["nbr_tour"]
        total = tournoi["nbr_jr"]
        print(f'{"=" * 119}')
        print(f'{"* MENU TOURNOIS*"}'.center(119))
        if tournoi and tournoi["nom"]:
            print("###### TOURNOI : ", tournoi["nom"], "| JOUEURS : ",
                  self.nbr_jr_ajoutes(tournoi), "| TOURS : ",
                  nbr_tours, "/", max_tour)
        print("1. Ajouter des joueurs.")
        if total == nbr_jrs and nbr_tours < max_tour:
            print("2. Lancer le TOUR N° :", (len(tournoi["tours"]) + 1))
        elif max_tour == nbr_tours:
            print("*. Le Tournoi est terminé ! ")
        else:
            print("____Le tournoi commencera avec tour 1____ ")
        print("3. Afficher la liste des participants par classement.")
        print("4. Afficher la liste des participants par ordre alphabétique.")
        print("5. Afficher la liste de tours et tous les matchs du tour.")
        print("0. Quitter le tournoi.")
        print(f'{"=" * 119}')

    @staticmethod
    def get_choix(nbrchoix):
        choix = ""
        while choix not in range(nbrchoix):
            try:
                choix = int(input("Choisissez ce que vous souhaitez faire :"))
            except (ValueError, TypeError):
                print("Désolé votre réponse n'est pas valide")
        return choix

    @staticmethod
    def exit_program():
        print("Merci d'avoir utilisé ce programme, à bientôt !")

    @staticmethod
    def get_input(self, attribut_1, attribut_2):
        value = ""
        value = input(f"Veuillez saisir {attribut_1} du {attribut_2}: ")
        if not value:
            print("Votre saisie n'a pas été comprise")
            value = input(f"veuillez rééssayer d'indiquer {attribut_1}"
                          f" du {attribut_2}: ")
        else:
            print(f"{attribut_1} du {attribut_2} est : {value}")
            return value

    @staticmethod
    def get_date(self, a1, a2):
        value = ""
        while not datetime_to_str(is_valid_date(value)):
            value = input(f"Veuillez saisir {a1} du {a2}: "
                          f"au format dd/MM/yyyy : ")
            if not value:
                print("Votre saisie n'a pas "
                      "été comprise")
                print(f"veuillez rééssayer d'indiquer {a1} du {a2} "
                      f"au format dd/MM/yyyy : ")
            else:
                if datetime_to_str(is_valid_date(value)):
                    print(f"{a1} du {a2} est : {value}")
                    return value
