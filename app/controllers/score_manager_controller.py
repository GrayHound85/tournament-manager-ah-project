from PyQt6.QtCore import QObject, pyqtSignal
import random

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
        self.__players_per_match = 4
        self.__matches_generated = False

    
    def request_fixture_generation(self, num_of_rounds: int = 10):
        if num_of_rounds > 128:
            return
        
        for round in range(num_of_rounds):
            participants = self.__participant_repo.get_participant_list().copy()
            random.shuffle(participants)

            for i in range(0, len(participants), self.__players_per_match):
                group = participants[i:i+self.__players_per_match]

                self.__match_repo.create_match(round + 1, group)
        
        
        self.fixturesGenerated.emit()