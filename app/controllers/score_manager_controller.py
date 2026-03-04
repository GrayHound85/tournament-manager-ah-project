from PyQt6.QtCore import QObject, pyqtSignal
from utils.standard_algorithms import StandardAlgorithms
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

    
    def request_fixture_generation(self, num_of_rounds: int = 10):
        if num_of_rounds > 128 or self.__match_repo.fixtures_generated() or num_of_rounds < 1:
            return
        
        for round in range(num_of_rounds):
            participants = self.__participant_repo.get_participant_list().copy()
            random.shuffle(participants)

            for i in range(0, len(participants), self.__players_per_match):
                group = participants[i:i+self.__players_per_match]

                self.__match_repo.create_match(round + 1, group)
        
        
        self.fixturesGenerated.emit()


    def fixtures_generated(self) -> bool:
        result = self.__match_repo.fixtures_generated()
        if result:
            self.fixturesGenerated.emit()
        return result
    

    def get_match(self, index):
        return self.__match_repo.get_matches()[index]
    

    def get_matches(self):
        return self.__match_repo.get_matches()


    def get_participant_name(self, participant_id: int) -> str:
        participant_list = self.__participant_repo.get_participant_list().copy()
        participant_list = StandardAlgorithms.insertion_sort(participant_list, "id")
        participant_index = StandardAlgorithms.binary_search(participant_list, "id", participant_id)
        participant = participant_list[participant_index]
        return participant.get_name()

    def get_participant_score(self, match_index: int, participant_id: int) -> int:
        return self.__match_repo.get_score(match_index, participant_id)
    
    def set_match_scores(self, match_index: int, participant_scores: dict) -> None:
        self.__match_repo.set_match_scores(match_index, participant_scores)