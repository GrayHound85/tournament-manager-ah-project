from PyQt6.QtWidgets import QWidget, QFrame, QVBoxLayout, QHBoxLayout, QSizePolicy, QLabel
from utils.ui_styler import UIStyler

from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from controllers.tournament_selector_controller import TournamentSelectorController

class TournamentSelectorScreen(QWidget, UIStyler):
    def __init__(self, controller: "TournamentSelectorController"):
        super().__init__()
        self.__controller = controller

        self.setup_ui()
    
    def setup_ui(self):
        root_layout = QVBoxLayout(self)
        root_layout.setContentsMargins(0,0,0,0)

        # Background
        frame = QFrame(self)
        frame.setSizePolicy(
            QSizePolicy.Policy.Expanding, 
            QSizePolicy.Policy.Expanding
            )
        self.style_primary_frame(frame)
        root_layout.addWidget(frame)

        # Main content -------------------------
        content_layout = QVBoxLayout(frame)
        self.set_screen_margin(content_layout)

        title_label = QLabel("Tournament Manager")
        content_layout.addWidget(title_label, 15)

        line = QFrame()
        line.setFrameShape(QFrame.Shape.HLine)
        content_layout.addWidget(line, 10)
        hbox = QHBoxLayout()
        content_layout.addLayout(hbox, 75)