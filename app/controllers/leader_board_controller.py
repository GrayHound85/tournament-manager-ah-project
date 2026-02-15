from PyQt6.QtCore import QObject, pyqtSignal
from utils.standard_algorithms import StandardAlgorithms

from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from repos.participant_repo import ParticipantRepo
    from repos.match_repo import MatchRepo

class LeaderBoardController(QObject):
    def __init__(self, participant_repo, match_repo):
        super().__init__()
        self.__participant_repo: ParticipantRepo = participant_repo
        self.__match_repo: MatchRepo = match_repo