from PyQt6.QtCore import QObject, pyqtSignal
from utils.standard_algorithms import StandardAlgorithms

from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from repos.participant_repo import ParticipantRepo

class ParticipantManagerController(QObject):
    addValidationResult = pyqtSignal(str, object)
    deleteValidationResult = pyqtSignal(str, str)

    def __init__(self, participant_repo):
        super().__init__()
        self.__participant_repo: ParticipantRepo = participant_repo
    
    
    def add_participant_requested(self, name: str) -> None:
        validation_result = self._validate_add_participant_request(name)
        participant = -1
        if validation_result == "":
            participant = self.__participant_repo.add_participant(name)
        
        self.addValidationResult.emit(validation_result, participant)


    def delete_participant_request(self, name: str) -> None:
        name_exists: int = StandardAlgorithms.binary_search(self.__participant_repo.get_participant_list(), "name", name)
        validation_result = self._validate_delete_participant_request(name, name_exists)
        if validation_result == "":
            self.__participant_repo.delete_participant(name_exists)

        self.deleteValidationResult.emit(validation_result, name)


    def _validate_add_participant_request(self, name: str) -> str:
        name_exists = StandardAlgorithms.binary_search(self.__participant_repo.get_participant_list(), "name", name)
        no_special_charcters = True
        for character in name:
            if (ord(character) < 97 or ord(character) > 122) and (ord(character) > 90 or ord(character) < 65) and ord(character) != 32:
                no_special_charcters = False

        if name_exists != -1:
            return "Name must be unique"
        elif no_special_charcters == False:
            return "Name can only contain: \n- Letters \n- Spaces"
        elif len(name) < 3:
            return "Must have at least 3 characters"
        elif len(name) > 255:
            return "Exeeded 255 character limit"
        elif len(self.__participant_repo.get_participant_list()) >= 1024:
            return "You have reached the particpant count limit of 1024"
        else: 
            return ""
        

    def _validate_delete_participant_request(self, name: str, name_exists) -> str:
        if name_exists == -1:
            return "Participant does not exist"
        elif len(name) < 3:
            return "Must have at least 3 characters"
        elif len(name) > 255:
            return "Exeeded 255 character limit"
        else:
            return ""
        

    def get_participant_list(self) -> list:
        return self.__participant_repo.get_participant_list()