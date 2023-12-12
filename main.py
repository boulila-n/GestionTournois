from controllers.joueurController import JoueurController
from controllers.tournoisController import TournoisContoller
import sys
from services.servicetournois import ServiceTournois


class Main:

    def __init__(self):
        self.joueur_controller = JoueurController()
        self.tournois_controller = TournoisContoller()
        self.service_tournoi = ServiceTournois()

    def menu_principal(self):
        choix = ""
        while choix != 0:
            self.joueur_controller.joueur_view.print_menu()
            choix = self.joueur_controller.joueur_view.get_choix(9)
            self.appliquer_choix(choix)

    def menu_tournois(self, tournoi):
        choix = ""
        while choix != 0:
            self.tournois_controller.tournois_view.print_menu_tournois(tournoi)
            choix = self.tournois_controller.tournois_view.get_choix(7)
            self.appliquer_choix_tournois(choix, tournoi)

    def appliquer_choix(self, user_choix: int):
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
        elif user_choix == 6:
            self.tournois_controller.afficher_liste_tournois()
        elif user_choix == 7:
            self.tournois_controller.get_tournoi_nom()
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
            self.tournois_controller.sort_joueur_score(tournoi)
        elif user_choix == 4:
            self.tournois_controller.get_sorted_joueurs(tournoi)
        elif user_choix == 5:
            self.tournois_controller.get_tous_tours(tournoi)
        elif user_choix == 0:
            self.menu_principal()
        else:
            pass

    def exit_program(self):
        confirm = self.tournois_controller.get_confirmation()
        if confirm == "Y":
            self.joueur_controller.joueur_view.exit_program()
            sys.exit()
        else:
            self.menu_principal()

    def ajouter_nv_joueur(self, tournoi):
        if tournoi:
            nbr = len(tournoi["list_joueur"])
            total = tournoi["nbr_jr"]
            tr = self.service_tournoi.deserialize_tournois(tournoi)
            if total - nbr > 0:
                idj = self.sasie_joueur_id()
                inserted_jr = self.joueur_controller.get_joueur_id(idj)
                inserted_jr["id"] = idj
                inserted_jr["opposants"] = []
                if inserted_jr:
                    tr.list_joueur.append(inserted_jr)
                else:
                    print("Joueur introuvable dans la base,"
                          " veuillez réssayer !")
            else:
                print(" *** La liste joueurs est compelte ***")

            self.tournois_controller.update_tournoi(tr)
        else:
            self.joueur_controller.get_joueur_infos()

    def sasie_joueur_id(self):
        self.afficher_joueurs()
        idj = input(print(f'{"Veuillez saisir lid de joueur à ajouter "}'
                          f'{"ou Entrer vide pour saisir"}'
                          f'{" un nouveau joueur : "}'))
        if not idj:
            return self.joueur_controller.get_joueur_infos()
        else:
            return idj

    def afficher_joueurs(self):
        self.joueur_controller.sort_joueurs_alpha()

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
        nbr = len(tr["tours"])
        joueurs = len(tr["list_joueur"])
        nbrj = tr["nbr_jr"]
        max = tr["nbr_tour"]
        if nbr < max and nbrj == joueurs:
            db_tr = self.tournois_controller.creer_tour(tr, nbr+1)
            self.menu_tournois(db_tr)
        else:
            print("### Veuillez vérifier votre choix ###")


if __name__ == "__main__":
    main = Main()
    main.menu_principal()
