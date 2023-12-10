

class TournoisView:

    def __int__(self):
        pass

    @staticmethod
    def print_titles():
        print("")
        print(f'{"=" * 140}')
        print(
            f"{'Id'.center(4)} | "
            f"{'Nom'.center(15)} | "
            f"{'Lieu'.center(12)} | "
            f"{'Date de début'.center(13)} | "
            f"{'Date de fin'.center(13)} | "
            f"{'Description'.center(20)} | "
            f"{'Nbre de joueurs'.center(10)} "
            f"\n{'*' * 140}")

    @staticmethod
    def afficher_tournement(
            id: int,
            nom: str,
            lieu: str,
            date_debut: str,
            date_fin: str,
            description: str,
            nbr_jr: int
    ):
        '''Displays tournament info in a table.

        '''
        print(
            f"{str(id).center(4)} | "
            f"{nom.center(15)} | "
            f"{lieu.center(12)} | "
            f"{date_debut.center(13)} | "
            f"{date_fin.center(13)} | "
            f"{description.center(20)} | "
            f"{str(nbr_jr).center(13)} "
            f"\n{'-' * 140}"
            f"\n{''}")

    def get_string_value(self, first_argument: str, second_argument: str):
        value = input(f"Veuillez saisir {first_argument} "
                      f"du {second_argument}: ")
        if not value:
            print("Votre saisie n'a pas été comprise")
            print(f"veuillez rééssayer d'indiquer {first_argument}"
                  f" du {second_argument}")
        else:
            return value

    def get_default_value(self, first_argument: str, second_argument: str):
        value = input(f"Veuillez saisir {first_argument} "
                      f"du {second_argument}: ")
        if value and not value.isnumeric():
            value = input(f"Veuillez saisir {first_argument} "
                          f"du {second_argument}: ")
        else:
            return value

    @staticmethod
    def print_tour_infos(
            nom: str
    ):
        print(
            f"{nom.center(20)}"
            f"\n{'*' * 85}")

    @staticmethod
    def print_match_infos(
            indx: int,
            joueur_1: str,
            score_joueur_1: float,
            joueur_2: str,
            score_joueur_2: float
    ):
        print(
            f"* Match {indx} : "
            f"{joueur_1.center(20)} vs "
            f"{joueur_2.center(20)} "
            f"{score_joueur_1} - "
            f"{score_joueur_2}"
            f"\n")

    @staticmethod
    def print_jr_infos(
            nom: str,
            prenom: str,
            date_naissance: str,
            points: float
    ):
        print(
            f"{nom.center(25)} | "
            f"{prenom.center(25)} | "
            f"{date_naissance.center(25)} | "
            f"{points}"
            f"\n{'-' * 119}")

    @staticmethod
    def print_titles_jr():
        print("")
        print(f'{"=" * 119}')
        print(
            f"{'NOM'.center(25)} | "
            f"{'PRENOM'.center(25)} | "
            f"{'date_naissance'.center(25)} | "
            f"{'SCORE'.center(20)}"
            f"\n{'*' * 119}")

    @staticmethod
    def print_titles_tour():
        print("")
        print(f'{"=" * 119}')
        print(
            f"{'LISTE DES TOURS'.center(25)}"
            f"\n{'*' * 119}")
