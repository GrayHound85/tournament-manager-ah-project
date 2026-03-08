from PyQt6.QtCore import QObject, pyqtSignal
from models.leader_board_model import LeaderBoardModel
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
        self.__model = LeaderBoardModel()

    def get_model(self):
        return self.__model
    
    def update_scores(self):
        data = []
        for participant in self.__participant_repo.get_participant_list():
            participant_id = participant.get_id()
            participant_name = participant.get_name()
            participant_score = self.__match_repo.get_total_score_for_participant(participant_id)
            participant_data = (participant_name, participant_score)
            data.append(participant_data)
        
        data = StandardAlgorithms.insertion_sort(data, 1, True)

        self.__model.update_data(data)

    def export_to_csv(self, export_path):
        data = self.__model.get_data()
        with open(export_path[0]+".csv", "w") as file:
            file.write("Rank,Name,Score\n")

            for rank, (name, score) in enumerate(data, start=1):
                line = f"{rank},{name},{score}\n"
                file.write(line)