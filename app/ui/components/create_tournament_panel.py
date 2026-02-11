from PyQt6.QtWidgets import QWidget, QLabel, QVBoxLayout, QLineEdit, QPushButton
from PyQt6.QtCore import Qt
from utils.ui_styler import UIStyler

class CreateTournamentPanel(QWidget, UIStyler):
    def __init__(self):
        super().__init__()
        self.setup_ui()

    def setup_ui(self):
        panel_layout = QVBoxLayout(self)
        panel_layout.setContentsMargins(70,50,70,70)

        header_label = QLabel("Create Tournament")
        self.set_font_heading(header_label, "35px")

        tournament_name_input = QLineEdit()
        tournament_name_input.setPlaceholderText("Enter tournament name")
        self.style_line_edit(tournament_name_input, "20px")
        tournament_name_input.setFixedHeight(50)

        validation_error_label = QLabel("This will only appear when validtion fails")
        self.style_error_label(validation_error_label)

        submit_button = QPushButton("Submit")
        self.style_button(submit_button, "25px")
        submit_button.setFixedSize(200, 65)


        panel_layout.addWidget(header_label)
        panel_layout.addSpacing(20)
        panel_layout.addWidget(tournament_name_input)
        panel_layout.addWidget(validation_error_label)
        panel_layout.addStretch()
        panel_layout.addWidget(submit_button)

        validation_error_label.setText("")
        
