from controllers.joueurController import JoueurController
from controllers.tournoisController import TournoisContoller
import sys
from services.servicetournois import ServiceTournois


class Main:

    def __init__(self):
        self.joueur_controller = JoueurController()
        self.tournois_controller = TournoisContoller()
        self.service_tornoi = ServiceTournois()

    def menu_principal(self):
        choix = ""
        while choix != 0:
            self.joueur_controller.menu_view.print_menu()
            choix = self.joueur_controller.menu_view.get_choix(6)
            self.appliquer_choix(choix)

    def menu_tournois(self,tournoi):
        choix = ""
        while choix != 0:
            self.tournois_controller.menu_view.print_menu_tournois(tournoi)
            choix = self.tournois_controller.menu_view.get_choix(6)
            self.appliquer_choix_tournois(choix,tournoi)

    def appliquer_choix(self, user_choix:int):
        if user_choix == 1:
            self.ajouter_nv_joueur(tournoi=None)
        elif user_choix == 2:
            self.afficher_joueurs()
        elif user_choix == 3:
            self.modifier_joueur()
        elif user_choix == 4:
            self.creer_tournois()
        elif user_choix == 5:
            self.reprendre_tournois()
        elif user_choix == 0:
            self.exit_program()
        else:
            pass

    def appliquer_choix_tournois(self, user_choix: int, tournoi):
        if user_choix == 1:
            self.ajouter_nv_joueur(tournoi)
        elif user_choix == 2:
            self.lancer_tour(tournoi)
        elif user_choix == 3:
            print("Afficher la liste des participants par classement.")
        elif user_choix == 4:
            print("Afficher la liste des participants par ordre alphabétique.")
        elif user_choix == 0:
            self.menu_principal()
        else:
            pass


    def exit_program(self):
        self.joueur_controller.menu_view.exit_program()
        sys.exit()

    def ajouter_nv_joueur(self, tournoi):
        if tournoi:
            nbr = len(tournoi["list_joueur"])
            total = tournoi["nbr_jr"]
            tr = self.service_tornoi.deserialize_tournois(tournoi)
            if total - nbr > 0:
                idj = self.joueur_controller.get_joueur_infos()
                inserted_jr = self.joueur_controller.get_joueur_id(idj)
                tr.list_joueur.append(inserted_jr)
            else:
                print(f'{"/" * 119}')
                print(" *** La liste joueurs est compelte, vous pouvez lancez les tours de matchs ****")
                print(f'{"/" * 119}')

            self.tournois_controller.update_tournoi(tr)
        else:
            self.joueur_controller.get_joueur_infos()

    def afficher_joueurs(self):
        self.joueur_controller.get_table()

    def modifier_joueur(self):
        self.joueur_controller.modifier()

    def creer_tournois(self):
        tr = self.tournois_controller.creer_tournois()
        self.menu_tournois(tr)

    def reprendre_tournois(self):
        nbr = self.tournois_controller.afficher_liste_tournois()
        if nbr and nbr > 0:
            id = self.tournois_controller.selectioner_tournoi()
            select_tournoi = self.tournois_controller.get_tournoi_id(id)
            if select_tournoi:
                print("Tournoi trouvé :", select_tournoi["nom"])
                self.menu_tournois(select_tournoi)
            else:
                print("Aucun tournoi trouvé!")
        else:
            print("Liste de tournois vide")

    def lancer_tour(self, tr):
        matchs = self.tournois_controller.random_matchs(tr)
        if matchs:
            for m in matchs:
                self.tournois_controller.start_match(m)
        self.menu_tournois(tr)


if __name__ == "__main__":
    main = Main()
    main.menu_principal()