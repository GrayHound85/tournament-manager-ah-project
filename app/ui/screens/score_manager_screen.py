from PyQt6.QtWidgets import QWidget, QFrame, QVBoxLayout, QSizePolicy, QLabel
from utils.ui_styler import UIStyler

from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from controllers.score_manager_controller import ScoreManagerController


class ScoreManagerScreen(QWidget, UIStyler):
    def __init__(self, controller: "ScoreManagerController"):
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

        test_label = QLabel("Score manager screen")
        root_layout.addWidget(test_label)