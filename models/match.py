
class Match:

    def __init__(self, joueur_1, joueur_2, score_joueur_1, score_joueur_2, score_gagnant=1, score_perdant=0, score_egalite=0.5):
        """constructor"""
        self.joueur_1 = joueur_1
        self.joueur_2 = score_joueur_2
        self.score_joueur_1 = score_joueur_1
        self.score_joueur_2 = score_joueur_2
        self.matchs = ([joueur_1,score_joueur_1],[joueur_2,score_joueur_2])
        self.score_gagnant = score_gagnant
        self.score_perdant = score_perdant
        self.score_egalite = score_egalite
