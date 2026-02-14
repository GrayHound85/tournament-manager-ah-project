from PyQt6.QtWidgets import QWidget, QLabel, QVBoxLayout, QHBoxLayout, QPushButton, QScrollArea, QFrame
from PyQt6.QtCore import pyqtSignal, Qt
from PyQt6.QtGui import QIcon
from utils.ui_styler import UIStyler

class OpenTournamentPanel(QWidget, UIStyler):
    openClicked = pyqtSignal(str)
    deleteClicked = pyqtSignal(str)

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
        scroll_content.setContentsMargins(0,0,0,0)

        panel_layout.addWidget(header_label)
        panel_layout.addSpacing(6)
        panel_layout.addWidget(scroll_area)
        self.tournament_row_layout = QVBoxLayout(scroll_content)
        self.tournament_row_layout.setAlignment(Qt.AlignmentFlag.AlignTop)
        self.tournament_row_layout.setSpacing(10)
        scroll_area.setWidget(scroll_content)

    
    def display_tournaments(self, tournaments: list[str]) -> None:
        self.__tournament_rows = {}
        if tournaments:
            for name in tournaments:
                self.__tournament_rows[name] = TournamentRow(name)
            
            for row in self.__tournament_rows.values():
                row.deleteClicked.connect(self.delete_tournament)
                row.openClicked.connect(self.open_tournament)
                self.tournament_row_layout.addWidget(row)
        else:
            print("You have not created a tournament yet")
    
    def delete_tournament(self, name):
        self.deleteClicked.emit(name)
        tournament = self.__tournament_rows.pop(name)
        self.tournament_row_layout.removeWidget(tournament)
        tournament.setParent(None)
        tournament.deleteLater()
    
    def open_tournament(self, name):
        self.openClicked.emit(name)

    

class TournamentRow(QFrame, UIStyler):
    openClicked = pyqtSignal(str)
    deleteClicked = pyqtSignal(str)

    def __init__(self, tournament_name):
        super().__init__()
        self.__name = tournament_name
        self.setup_ui()
    

    def setup_ui(self) -> None:
        self.style_panel_2(frame=self)
        self.setFixedHeight(60)
        self.setContentsMargins(0,0,0,0)
        open_button = QPushButton(self.__name)
        open_button.setFixedHeight(60)
        open_button.setFlat(True)
        open_button.clicked.connect(lambda: self.openClicked.emit(self.__name))
        self.style_button_2(open_button, "20px")
        layout = QHBoxLayout(self)
        layout.addWidget(open_button)
        layout.setContentsMargins(0,0,0,0)

        delete_button = QPushButton()
        delete_button.setFixedSize(60,60)
        delete_button.setFlat(True)
        delete_button.setIcon(QIcon.fromTheme("preferences-system"))
        delete_button.setIconSize(delete_button.size())
        delete_button.clicked.connect(lambda: self.deleteClicked.emit(self.__name))
        layout.addWidget(delete_button)

