from PyQt6.QtCore import QObject, pyqtSignal
from utils.standard_algorithms import StandardAlgorithms

# Enables type hinting for classes passed in.
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from repos.tournament_repo import TournamentRepo


class TournamentSelectorController(QObject):
    validationError = pyqtSignal(str)

    def __init__(self, tournament_repo):
        super().__init__()
        self.__tournament_repo: "TournamentRepo" = tournament_repo

    
    def get_all_tournament(self) -> list[str]:
        result = self.__tournament_repo.get_databases()
        db_names = [db[0] for db in result]
        return db_names
    
    def submit_tournament_creation(self, name) -> None:
        validation_result = self._validate_tournament_name(name)
        if validation_result == "":
            self.__tournament_repo.add_tournament(name)

        self.validationError.emit(validation_result)


    def _validate_tournament_name(self, name) -> str:
        tournament_names = self.get_all_tournament()
        if len(name) < 5:
            return "Must be at least 5 characters"
        elif len(name) >= 128:
            return "Can't be longer that 127 characters"
        elif name in tournament_names:
            return "Name already in use"
        else:
            return ""
    
