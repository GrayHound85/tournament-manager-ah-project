from PyQt6.QtCore import QObject, pyqtSignal

from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from repos.participant_repo import ParticipantRepo
    from repos.match_repo import MatchRepo

class ScoreManagerController(QObject):
    fixturesGenerated = pyqtSignal()

    def __init__(self, participant_repo, match_repo):
        super().__init__()
        self.__participant_repo: ParticipantRepo = participant_repo
        self.__match_repo: MatchRepo = match_repo

    
    def request_fixture_generation(self):
        self.fixturesGenerated.emit()