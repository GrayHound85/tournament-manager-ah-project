from PyQt6.QtWidgets import QWidget, QFrame, QVBoxLayout, QSizePolicy, QLabel
from utils.ui_styler import UIStyler

from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from controllers.leader_board_controller import LeaderBoardController


class LeaderBoardScreen(QWidget, UIStyler):
    def __init__(self, controller: "LeaderBoardController"):
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

        test_label = QLabel("Leader board screen")
        root_layout.addWidget(test_label)