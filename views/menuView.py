
from abc import ABC


class MenuView(ABC):

    @staticmethod
    def print_menu():
        print(f'{"=" * 119}')
        print(f'{"* MENU PRINCIPAL*"}'.center(119))
        print("1. Ajouter un nouveau joueur")
        print("2. Afficher la liste des joueurs")
        print("3. Modifier joueur")
        print("4. Créer un nouveau tournois")
        print("5. Reprendre un tournois")
        print("0. Quitter le programme")
        print(f'{"=" * 119}')

    def nbr_jr_ajoutes(self, tr):
        return str(len(tr["list_joueur"])) + " AJOUTES PARMI " + str(tr["nbr_jr"])
    def print_menu_tournois(self, tournoi):
        print(f'{"=" * 119}')
        print(f'{"* MENU TOURNOIS*"}'.center(119))
        if tournoi and tournoi["nom"]:
            print("###### TOURNOI : ", tournoi["nom"], " JOUEURS : " , self.nbr_jr_ajoutes(tournoi))
        print("1. Ajouter des joueurs.")
        print("2. Afficher la liste des participants par classement.")
        print("3. Afficher la liste des participants par ordre alphabétique.")
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
            print(f"veuillez rééssayer d'indiquer {attribut_1} du {attribut_2}")
        else:
            print(f"{attribut_1} du {attribut_2} est : {value}")
            return value

