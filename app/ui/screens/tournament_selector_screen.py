from PyQt6.QtWidgets import QWidget
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from controllers.tournament_selector_controller import TournamentSelectorController

class TournamentSelectorScreen(QWidget):
    def __init__(self, tournament_selector_controller: TournamentSelectorController):
        super().__init__()
        self.__controller = tournament_selector_controller

        self.setup_ui(self)
    
    def setup_ui(self):
        pass