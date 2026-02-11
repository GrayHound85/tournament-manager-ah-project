from PyQt6.QtWidgets import QWidget, QLabel, QVBoxLayout, QHBoxLayout, QPushButton, QScrollArea, QSizePolicy
from PyQt6.QtCore import pyqtSignal, Qt
from utils.ui_styler import UIStyler

class OpenTournamentPanel(QWidget, UIStyler):
    def __init__(self):
        super().__init__()
        self.setup_ui()
    
    def setup_ui(self) -> None:
        panel_layout = QVBoxLayout(self)
        panel_layout.setSpacing(20)
        panel_layout.setContentsMargins(70,50,70,70)

        header_label = QLabel("Open Tournament")
        self.set_font_heading(header_label, "35px")

        scroll_area = QScrollArea()
        scroll_area.setWidgetResizable(True)
        self.style_scroll_area(scroll_area)

        scroll_content = QWidget()
        scroll_content.setStyleSheet("background: transparent;")

        panel_layout.addWidget(header_label)
        panel_layout.addSpacing(6)
        panel_layout.addWidget(scroll_area)
        self.tournament_row_layout = QVBoxLayout(scroll_content)
        self.tournament_row_layout.setAlignment(Qt.AlignmentFlag.AlignTop)
        scroll_area.setWidget(scroll_content)

    
    def display_tournaments(self, tournaments: list[str]) -> None:
        tournament_rows = {}
        if tournaments:
            for name in tournaments:
                tournament_rows[name] = TournamentRow(name)
            
            for row in tournament_rows.values():
                self.tournament_row_layout.addWidget(row)
        else:
            print("You have not created a tournament yet")
            

    

class TournamentRow(QWidget, UIStyler):
    def __init__(self, tournament_name):
        super().__init__()
        self.__name = tournament_name
        self.setup_ui()
    

    def setup_ui(self):
        button = QPushButton(self.__name)
        button.setFixedHeight(50)
        self.style_button_2(button, "20px")
        layout = QHBoxLayout(self)
        layout.addWidget(button)

