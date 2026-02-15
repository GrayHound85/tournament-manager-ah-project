from PyQt6.QtCore import QObject, pyqtSignal
from utils.standard_algorithms import StandardAlgorithms

from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from repos.participant_repo import ParticipantRepo

class ParticipantManagerController(QObject):
    def __init__(self, participant_repo):
        super().__init__()
        self.__participant_repo: ParticipantRepo = participant_repo