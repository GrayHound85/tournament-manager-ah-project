from PyQt6.QtWidgets import QWidget, QLabel, QVBoxLayout, QLineEdit, QPushButton
from PyQt6.QtCore import Qt, pyqtSignal
from utils.ui_styler import UIStyler

class CreateTournamentPanel(QWidget, UIStyler):
    submitPressed = pyqtSignal(str)

    def __init__(self):
        super().__init__()
        self.setup_ui()

    def setup_ui(self) -> None:
        panel_layout = QVBoxLayout(self)
        panel_layout.setContentsMargins(70,50,70,70)

        header_label = QLabel("Create Tournament")
        self.set_font_heading(header_label, "35px")

        tournament_name_input = QLineEdit()
        tournament_name_input.setPlaceholderText("Enter tournament name")
        self.style_line_edit(tournament_name_input, "20px")
        tournament_name_input.setFixedHeight(60)

        self.__validation_error_label = QLabel()
        self.style_error_label(self.__validation_error_label)

        submit_button = QPushButton("Submit")
        self.style_button(submit_button, "25px")
        submit_button.setFixedSize(200, 65)
        submit_button.clicked.connect(lambda: self.submitPressed.emit(tournament_name_input.text()))



        panel_layout.addWidget(header_label)
        panel_layout.addSpacing(20)
        panel_layout.addWidget(tournament_name_input)
        panel_layout.addWidget(self.__validation_error_label)
        panel_layout.addStretch()
        panel_layout.addWidget(submit_button)

    def handle_validation_result(self, result: str) -> None:
        self.__validation_error_label.setText(result)
