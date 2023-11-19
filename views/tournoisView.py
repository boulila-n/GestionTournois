

class TournoisView:

    def __int__(self):
        pass

    @staticmethod
    def display_tournament_header():
        '''Displays the tournaments table header.

        '''
        print("")
        print(f'{"=" * 140}')
        print(
            f"{'Id'.center(4)} | "
            f"{'Nom'.center(15)} | "
            f"{'Lieu'.center(12)} | "
            f"{'Date de début'.center(13)} | "
            f"{'Date de fin'.center(13)} | "
            f"{'Time control'.center(13)} | "
            f"{'Nbre de tours'.center(10)} | "
            f"{'Nbre joueur max'.center(10)} | "
            f"{'Description'.center(20)}"
            f"\n{'*' * 140}")

    @staticmethod
    def display_tournament(
            numero: int,
            nom: str,
            lieu: str,
            date_debut: str,
            date_fin: str,
            nbr_tour: int,
            description: str
    ):
        '''Displays tournament info in a table.

        '''
        print(
            f"{str(numero).center(4)} | "
            f"{nom.center(15)} | "
            f"{lieu.center(12)} | "
            f"{date_debut.center(13)} | "
            f"{date_fin.center(13)} | "
            f"{str(nbr_tour).center(13)} | "
            f"{description.center(20)}"
            f"\n{'-' * 140}"
            f"\n{''}")

    def get_string_value(self, first_argument: str, second_argument: str):

            value = input(f"Veuillez saisir {first_argument} du {second_argument}: ")
            if not value:
                print("Votre saisie n'a pas été comprise")
                print(
                    f"veuillez rééssayer d'indiquer {first_argument} du {second_argument}"
                )
            else:
                return value


