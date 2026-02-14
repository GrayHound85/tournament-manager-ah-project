from PyQt6.QtCore import QObject, pyqtSignal
from utils.standard_algorithms import StandardAlgorithms

# Enables type hinting for classes passed in.
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from repos.tournament_repo import TournamentRepo


class TournamentSelectorController(QObject):
    validationError = pyqtSignal(str)
    openTournament = pyqtSignal()

    def __init__(self, repo):
        super().__init__()
        self.__tournament_repo: "TournamentRepo" = repo
        self.__tournament_name_suffix = "_td"

    
    def get_all_tournament(self) -> list[str]:
        result = self.__tournament_repo.get_databases()
        db_names = [db[0] for db in result]
        tournament_names = []
        for name in db_names:
            if name[-3:] == self.__tournament_name_suffix:
                tournament_names.append(name[:-3])

        return tournament_names
    
    
    def open_tournament_request(self, name: str) -> None:
        self.__tournament_repo.open_tournament(name + self.__tournament_name_suffix)
    

    def delete_tournament_request(self, name: str) -> None:
        self.__tournament_repo.delete_tournament(name + self.__tournament_name_suffix)

    
    def submit_tournament_creation(self, name: str) -> None:
        validation_result = self._validate_tournament_name(name)
        if validation_result == "":
            db_name = name + self.__tournament_name_suffix
            self.__tournament_repo.add_tournament(db_name)
            self.openTournament.emit()

        self.validationError.emit(validation_result)


    def _validate_tournament_name(self, name) -> str:
        tournament_names = self.get_all_tournament()
        no_special_charcters = True
        for character in name:
            if ord(character) != 95 and (ord(character) < 97 or ord(character) > 122) and (ord(character) < 48 or ord(character) > 57):
                no_special_charcters = False

        if len(name) < 5:
            return "Must be at least 5 characters"
        elif len(name) >= 128:
            return "Must be under 128 characters"
        elif name in tournament_names:
            return "Name already in use"
        elif no_special_charcters == False:
            return "Name can only contain: \n- Lowercase letters \n- Numbers \n- _"
        else:
            return ""
    
