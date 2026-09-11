from models.subject import Sujet


DUREE_TRAVAIL = 25 * 60
DUREE_PAUSE = 5 * 60


class Minuteur(Sujet):

    def __init__(self):
        super().__init__()
        self._temps_restant = DUREE_TRAVAIL
        self._en_pause = False
        self._etat = "Travail"   # "Travail" ou "Pause"
        self._sessions_completees = 0

    def tick(self) -> None:
        """Avance le minuteur d'une seconde et notifie les observateurs."""
        # À compléter :
        # 1. Si en pause, ne rien faire
        if self._en_pause == True:
            return
        # 2. Si temps_restant > 0, décrémenter
        if self._temps_restant > 0:
            self._temps_restant -= 1
        # 3. Sinon, appeler _changer_etat()
        else:
            self._changer_etat()
        # 4. Notifier les observateurs
        self.notifier()
        

    def _changer_etat(self) -> None:
        """Bascule entre travail et pause."""
        # À compléter :
        # Si état == "Travail" : incrémenter sessions, passer en "Pause", reset temps
        if self._etat == "Travail" and self._temps_restant == 0:
            self._sessions_completes += 1
            self._en_pause = True
            self._etat = "Pause"
            self._temps_restant = DUREE_PAUSE
        # Sinon : passer en "Travail", reset temps
        else:
            self._etat = "Travail"
            self._temps_restant = DUREE_TRAVAIL

    def basculer_pause(self) -> None:
        """Met en pause ou reprend le minuteur."""
        if self._etat == "Travail":
            self._etat = "Pause"

        if self._etat == "Pause":
            self._etat = "Travail"

    def reinitialiser(self) -> None:
        """Réinitialise le minuteur à l'état initial."""
        # À compléter
        # N'oubliez pas de notifier les observateurs à la fin
        self._temps_restant = DUREE_TRAVAIL
        self._en_pause = False
        self._etat = "Travail"
        self._sessions_completees = 0
        self.notifier()

    def get_donnees(self) -> dict:
        # À compléter : retourner un dictionnaire avec :
        # temps_restant, etat, en_pause, sessions_completees, duree_totale
        if self._etat == "Travail":
           duree_totale = DUREE_TRAVAIL * self._sessions_completees
        else:
           duree_totale = DUREE_PAUSE * self._sessions_completees

        return {
           "temps_restant": self._temps_restant,
           "etat": self._etat,
           "en_pause": self._en_pause,
           "sessions_completees": self._sessions_completees,
           "duree_totale": duree_totale,
        }

        return donnees
