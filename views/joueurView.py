

class JoueurView:

    def __int__(self):
        pass

    @staticmethod
    def print_titles():
        print("")
        print(f'{"=" * 119}')
        print(
            f"{'ID'.center(10)} | "
            f"{'NOM'.center(25)} | "
            f"{'PRENOM'.center(25)} | "
            f"{'DATE_DE_NAISSANCE'.center(20)} | "
            f"\n{'*' * 119}")
    @staticmethod
    def print_jr_infos(
            id: int,
            nom: str,
            prenom: str,
            date_naissance: str
    ):
        print(
            f"{str(id).center(10)} | "
            f"{nom.center(25)} | "
            f"{prenom.center(25)} | "
            f"{date_naissance.center(20)} | "
            f"\n{'-' * 119}")