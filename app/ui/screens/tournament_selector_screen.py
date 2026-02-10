from PyQt6.QtWidgets import QWidget, QFrame, QVBoxLayout, QHBoxLayout, QSizePolicy, QLabel
from PyQt6.QtCore import Qt
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
        self.set_font_heading(title_label)
        content_layout.addWidget(title_label, 15)
        title_label.setAlignment(Qt.AlignmentFlag.AlignCenter)

        h_line = QFrame()
        h_line.setFrameShape(QFrame.Shape.HLine)
        self.style_seperator_line(h_line, 1400)
        content_layout.addWidget(h_line, 10, alignment=Qt.AlignmentFlag.AlignHCenter)
        hbox = QHBoxLayout()
        content_layout.addLayout(hbox, 75)

        # Content panels
        panel_1_container = QFrame()
        panel_1_container.setSizePolicy(
            QSizePolicy.Policy.Expanding,
            QSizePolicy.Policy.Expanding
        )

        panel_1_layout = QVBoxLayout(panel_1_container)
        panel_1_layout.setContentsMargins(40, 40, 40, 40)
        panel_1_layout.setAlignment(Qt.AlignmentFlag.AlignCenter)
        panel_1 = QFrame()
        panel_1.setSizePolicy(
            QSizePolicy.Policy.Expanding,
            QSizePolicy.Policy.Expanding
        )
        self.style_panel(panel_1)
        panel_1_layout.addWidget(panel_1)
        hbox.addWidget(panel_1_container, 45)

        v_line = QFrame()
        v_line.setFrameShape(QFrame.Shape.VLine)
        self.style_seperator_line(v_line, 400)
        hbox.addWidget(v_line, 10)

        panel_2_container = QFrame()
        panel_2_container.setSizePolicy(
            QSizePolicy.Policy.Expanding,
            QSizePolicy.Policy.Expanding
        )

        panel_2_layout = QVBoxLayout(panel_2_container)
        panel_2_layout.setContentsMargins(40, 40, 40, 40)
        panel_2_layout.setAlignment(Qt.AlignmentFlag.AlignCenter)

        panel_2 = QFrame()
        panel_2.setSizePolicy(
            QSizePolicy.Policy.Expanding,
            QSizePolicy.Policy.Expanding
        )
        self.style_panel(panel_2)

        panel_2_layout.addWidget(panel_2)
        hbox.addWidget(panel_2_container, 45)


        # Create or open tournament buttons
