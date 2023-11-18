from controllers.joueurController import JoueurController
import sys

class Main:

    def __init__(self):
        self.joueur_controller = JoueurController()

    def menu(self):
        choix = ""
        while choix != 0:
            self.joueur_controller.menu_view.print_menu()
            choix = self.joueur_controller.menu_view.get_choix(3)
            self.appliquer_choix(choix)

    def appliquer_choix(self, user_choix:int):
        if user_choix == 1:
            self.ajouter_nv_jr()
        elif user_choix == 2:
            self.afficher_joueurs()
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


if __name__ == "__main__":
    main = Main()
    main.menu()