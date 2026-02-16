from PyQt6.QtWidgets import QWidget, QFrame, QVBoxLayout, QHBoxLayout, QSizePolicy, QLabel, QLineEdit, QPushButton, QScrollArea
from PyQt6.QtCore import Qt
from utils.ui_styler import UIStyler

from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from controllers.participant_manager_controller import ParticipantManagerController


class ParticipantManagerScreen(QWidget, UIStyler):
    def __init__(self, controller: "ParticipantManagerController"):
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

        # Content panels -----------------
        panel_layout = QHBoxLayout(frame)
        panel_layout.setContentsMargins(40,40,40,40)
        panel_layout.setSpacing(40)

        # Control panel
        control_panel = QFrame()
        self.style_panel(control_panel)
        control_panel_layout = QVBoxLayout(control_panel)
        control_panel_layout.setContentsMargins(40,20,40,35)

        heading = QLabel("Participant Manager")
        heading.setAlignment(Qt.AlignmentFlag.AlignTop | Qt.AlignmentFlag.AlignHCenter)
        heading.setContentsMargins(0,0,0,10)
        self.set_font_heading(heading, size="30px")

        seperator_line_1 = QFrame()
        seperator_line_1.setFrameShape(QFrame.Shape.HLine)
        self.style_seperator_line(seperator_line_1, 400)

        new_participant_input = QLineEdit()
        new_participant_input.setPlaceholderText("Enter new participant name")
        new_participant_input.setFixedHeight(60)
        self.style_line_edit(new_participant_input, "20px")

        submit_new_participant_button = QPushButton("Add participant")
        submit_new_participant_button.setFixedHeight(60)
        self.style_button(submit_new_participant_button, "20px")

        adding_participant_status_label = QLabel("")
        self.style_error_label(adding_participant_status_label)

        seperator_line_2 = QFrame()
        seperator_line_2.setFrameShape(QFrame.Shape.HLine)
        self.style_seperator_line(seperator_line_2, 400)

        participant_to_delete_input = QLineEdit()
        participant_to_delete_input.setPlaceholderText("Enter name of existing participant")
        participant_to_delete_input.setFixedHeight(60)
        self.style_line_edit(participant_to_delete_input, "20px")

        delete_participant_button = QPushButton("Delete participant")
        delete_participant_button.setFixedHeight(60)
        self.style_button(delete_participant_button, "20px")

        delete_participant_status_label = QLabel("")
        self.style_error_label(delete_participant_status_label)

        seperator_line_3 = QFrame()
        seperator_line_3.setFrameShape(QFrame.Shape.HLine)
        self.style_seperator_line(seperator_line_3, 400)

        participant_counter_container = QWidget()
        counter_layout = QHBoxLayout(participant_counter_container)
        counter_layout.setContentsMargins(0,0,0,0)
        static_label = QLabel("Total \nParticipants")
        self.set_font_heading(static_label, "20px")
        participant_count_label = QLabel("1024")
        participant_count_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.style_counter_label(participant_count_label, "30px")
        counter_layout.addWidget(static_label)
        counter_layout.addWidget(participant_count_label)

        control_panel_layout.addWidget(heading)
        control_panel_layout.addWidget(seperator_line_1, alignment=Qt.AlignmentFlag.AlignHCenter)
        control_panel_layout.addSpacing(20)
        control_panel_layout.addWidget(new_participant_input)
        control_panel_layout.addSpacing(20)
        control_panel_layout.addWidget(submit_new_participant_button)
        control_panel_layout.addSpacing(10)
        control_panel_layout.addWidget(adding_participant_status_label)
        control_panel_layout.addSpacing(20)
        #control_panel_layout.addWidget(seperator_line_2)
        control_panel_layout.addSpacing(20)
        control_panel_layout.addWidget(participant_to_delete_input)
        control_panel_layout.addSpacing(20)
        control_panel_layout.addWidget(delete_participant_button)
        control_panel_layout.addSpacing(10)
        control_panel_layout.addWidget(delete_participant_status_label)
        control_panel_layout.addStretch()
        control_panel_layout.addWidget(seperator_line_3)
        control_panel_layout.addSpacing(20)
        control_panel_layout.addWidget(participant_counter_container)

        # Participant display panel
        display_panel = QFrame()
        self.style_panel(display_panel)
        display_panel_layout = QVBoxLayout(display_panel)

        table_headings_container = QWidget()
        table_headings_layout = QHBoxLayout(table_headings_container)
        heading_id = QLabel("ID")
        self.set_font_heading(heading_id, "20px")
        heading_name = QLabel("Name")
        self.set_font_heading(heading_name, "20px")
        table_headings_layout.addSpacing(20)
        table_headings_layout.addWidget(heading_id,2)
        table_headings_layout.addWidget(heading_name,8)

        scroll_area = QScrollArea()
        scroll_area.setWidgetResizable(True)
        self.style_scroll_area(scroll_area)

        scroll_content = QWidget()
        scroll_content.setStyleSheet("background: transparent;")
        scroll_area.setWidget(scroll_content)

        display_panel_layout.addWidget(table_headings_container)
        display_panel_layout.addWidget(scroll_area)

        panel_layout.addWidget(control_panel, 1)
        panel_layout.addWidget(display_panel, 2)
