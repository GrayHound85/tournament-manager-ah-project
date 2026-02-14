from PyQt6.QtWidgets import QWidget, QFrame, QVBoxLayout, QHBoxLayout, QSizePolicy, QLabel, QPushButton, QStackedWidget
from PyQt6.QtCore import Qt, pyqtSignal
from utils.ui_styler import UIStyler
from ui.components.create_tournament_panel import CreateTournamentPanel
from ui.components.open_tourmanent_panel import OpenTournamentPanel

from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from controllers.tournament_selector_controller import TournamentSelectorController

class TournamentSelectorScreen(QWidget, UIStyler):
    openTournament = pyqtSignal()

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
        panel_1_content_layout = QVBoxLayout(panel_1)
        panel_1_content_layout.setAlignment(Qt.AlignmentFlag.AlignCenter)
        panel_1_content_layout.setSpacing(40)
        
        open_tournament_button = QPushButton("Open Tournament")
        open_tournament_button.setFixedSize(400,100)
        self.style_button(open_tournament_button, "25px")
        panel_1_content_layout.addWidget(open_tournament_button)
        open_tournament_button.clicked.connect(lambda: panel_stacker.setCurrentIndex(1))

        create_tournament_button = QPushButton("Create Tournament")
        create_tournament_button.setFixedSize(400, 100)
        self.style_button(create_tournament_button, "25px")
        panel_1_content_layout.addWidget(create_tournament_button)
        create_tournament_button.clicked.connect(lambda: panel_stacker.setCurrentIndex(0))

        # Create or open tournament panels
        panel_2_content_layout = QVBoxLayout(panel_2)
        panel_2_content_layout.setContentsMargins(0,0,0,0)

        panel_stacker = QStackedWidget()
        panel_2_content_layout.addWidget(panel_stacker)

        self.create_tournament_panel = CreateTournamentPanel() 
        self.create_tournament_panel.submitPressed.connect(self.__controller.submit_tournament_creation)
        self.__controller.validationError.connect(self.create_tournament_panel.handle_validation_result) 
        self.__controller.openTournament.connect(self.openTournament.emit)  
        panel_stacker.addWidget(self.create_tournament_panel)


        self.open_tournament_panel = OpenTournamentPanel()
        panel_stacker.addWidget(self.open_tournament_panel)
        self.open_tournament_panel.deleteClicked.connect(self.__controller.delete_tournament_request)
        self.open_tournament_panel.openClicked.connect(self.__controller.open_tournament_request)
        self.open_tournament_panel.openClicked.connect(self.openTournament.emit)
        self.open_tournament_panel.display_tournaments(self.__controller.get_all_tournament())

        