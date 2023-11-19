from controllers.joueurController import JoueurController
from controllers.tournoisController import TournoisContoller
import sys


class Main:

    def __init__(self):
        self.joueur_controller = JoueurController()
        self.tournois_controller = TournoisContoller()

    def menu(self):
        choix = ""
        while choix != 0:
            self.joueur_controller.menu_view.print_menu()
            choix = self.joueur_controller.menu_view.get_choix(5)
            self.appliquer_choix(choix)

    def menu_tournois(self):
        choix = ""
        while choix != 0:
            self.tournois_controller.menu_view.print_menu()
            choix = self.tournois_controller.menu_view.get_choix(5)
            self.appliquer_choix(choix)

    def appliquer_choix(self, user_choix:int):
        if user_choix == 1:
            self.ajouter_nv_jr()
        elif user_choix == 2:
            self.afficher_joueurs()
        elif user_choix == 3:
            self.modifier()
        elif user_choix == 4:
            self.create_tournois()
        elif user_choix == 0:
            self.exit_program()
        else:
            pass

    def exit_program(self):
        self.joueur_controller.menu_view.exit_program()
        sys.exit()

    def ajouter_nv_jr(self):
        self.joueur_controller.get_joueur_infos()

    def afficher_joueurs(self):
        self.joueur_controller.get_table()

    def modifier(self):
        self.joueur_controller.modifier()

    def create_tournois(self):
        self.tournois_controller.create()


if __name__ == "__main__":
    main = Main()
    main.menu()