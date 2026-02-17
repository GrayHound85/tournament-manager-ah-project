from PyQt6.QtCore import QObject, pyqtSignal
from utils.standard_algorithms import StandardAlgorithms

from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from repos.participant_repo import ParticipantRepo

class ParticipantManagerController(QObject):
    addValidationResult = pyqtSignal(str)
    deleteValidationResult = pyqtSignal(str)

    def __init__(self, participant_repo):
        super().__init__()
        self.__participant_repo: ParticipantRepo = participant_repo

    
    def add_participant_requested(self, name: str) -> None:
        validation_result = self._validate_add_participant_request(name)
        if validation_result == "":
            print(name)
        
        self.addValidationResult.emit(validation_result)


    def delete_participant_request(self, name: str) -> None:
        validation_result = self._validate_delete_participant_request(name)
        if validation_result == "":
            print(name)

        self.deleteValidationResult.emit(validation_result)


    def _validate_add_participant_request(self, name: str) -> str:
        name_exists = False
        contains_special_characters = False

        if name_exists:
            return "Name must be unique"
        elif contains_special_characters:
            return "Name can only contain: \n- Letters \n- Numbers \n- _, ', -"
        else: 
            return ""
        

    def _validate_delete_participant_request(self, name: str) -> str:
        name_exists = True
        if not name_exists:
            return "Participant does not exist"
        else:
            return ""