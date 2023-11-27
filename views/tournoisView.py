

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
            f"{'Nbre joueur max'.center(10)} "
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

            value = input(f"Veuillez saisir {first_argument} du {second_argument}: ")
            if not value:
                print("Votre saisie n'a pas été comprise")
                print(
                    f"veuillez rééssayer d'indiquer {first_argument} du {second_argument}"
                )
            else:
                return value


