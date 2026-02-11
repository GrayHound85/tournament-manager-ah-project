from PyQt6.QtWidgets import QWidget, QLabel, QVBoxLayout, QLineEdit, QPushButton
from utils.ui_styler import UIStyler

class CreateTournamentPanel(QWidget, UIStyler):
    def __init__(self):
        super().__init__()
        self.setup_ui()

    def setup_ui(self):
        panel_layout = QVBoxLayout(self)

        header_label = QLabel("Create Tournament")
        self.set_font_heading(header_label, "35px")

        tournmanet_name_input = QLineEdit("Enter tournament name")
        self.style_line_edit(tournmanet_name_input, "20px")
        tournmanet_name_input.setFixedHeight(50)

        validation_error_label = QLabel("This will only appear when validtion fails")
        self.style_error_label(validation_error_label)

        submit_button = QPushButton("Submit")
        self.style_button_default(submit_button, "25px")
        submit_button.setFixedSize(200, 65)


        panel_layout.addWidget(header_label)
        panel_layout.addWidget(tournmanet_name_input)
        panel_layout.addWidget(validation_error_label)
        panel_layout.addWidget(submit_button)
        
