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

        self.new_participant_input = QLineEdit()
        self.new_participant_input.setPlaceholderText("Enter new participant name")
        self.new_participant_input.setFixedHeight(60)
        self.style_line_edit(self.new_participant_input, "20px")

        self.__submit_new_participant_button = QPushButton("Add participant")
        self.__submit_new_participant_button.setFixedHeight(60)
        self.__submit_new_participant_button.clicked.connect(lambda: self.__controller.add_participant_requested(self.new_participant_input.text()))
        self.__controller.addValidationResult.connect(self._handle_add_participant_validation_result)
        self.style_button(self.__submit_new_participant_button, "20px")

        self.__adding_participant_status_label = QLabel("")
        self.style_error_label(self.__adding_participant_status_label)

        seperator_line_2 = QFrame()
        seperator_line_2.setFrameShape(QFrame.Shape.HLine)
        self.style_seperator_line(seperator_line_2, 400)

        self.participant_to_delete_input = QLineEdit()
        self.participant_to_delete_input.setPlaceholderText("Enter name of existing participant")
        self.participant_to_delete_input.setFixedHeight(60)
        self.style_line_edit(self.participant_to_delete_input, "20px")

        self.__delete_participant_button = QPushButton("Delete participant")
        self.__delete_participant_button.setFixedHeight(60)
        self.__delete_participant_button.clicked.connect(lambda: self.__controller.delete_participant_request(self.participant_to_delete_input.text()))
        self.__controller.deleteValidationResult.connect(self._handle_delete_participant_validation_result)
        self.style_button(self.__delete_participant_button, "20px")

        self.__delete_participant_status_label = QLabel("")
        self.style_error_label(self.__delete_participant_status_label)

        seperator_line_3 = QFrame()
        seperator_line_3.setFrameShape(QFrame.Shape.HLine)
        self.style_seperator_line(seperator_line_3, 400)

        participant_counter_container = QWidget()
        counter_layout = QHBoxLayout(participant_counter_container)
        counter_layout.setContentsMargins(0,0,0,0)
        static_label = QLabel("Total \nParticipants")
        self.set_font_heading(static_label, "20px")
        self.participant_count_label = QLabel("1024")
        self.participant_count_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.style_counter_label(self.participant_count_label, "30px")
        counter_layout.addWidget(static_label)
        counter_layout.addWidget(self.participant_count_label)

        control_panel_layout.addWidget(heading)
        control_panel_layout.addWidget(seperator_line_1, alignment=Qt.AlignmentFlag.AlignHCenter)
        control_panel_layout.addSpacing(20)
        control_panel_layout.addWidget(self.new_participant_input)
        control_panel_layout.addSpacing(20)
        control_panel_layout.addWidget(self.__submit_new_participant_button)
        control_panel_layout.addSpacing(10)
        control_panel_layout.addWidget(self.__adding_participant_status_label)
        control_panel_layout.addSpacing(20)
        #control_panel_layout.addWidget(seperator_line_2)
        control_panel_layout.addSpacing(20)
        control_panel_layout.addWidget(self.participant_to_delete_input)
        control_panel_layout.addSpacing(20)
        control_panel_layout.addWidget(self.__delete_participant_button)
        control_panel_layout.addSpacing(10)
        control_panel_layout.addWidget(self.__delete_participant_status_label)
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
        scroll_area.setHorizontalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOff)
        self.style_scroll_area(scroll_area)

        scroll_content = QWidget()
        scroll_content.setStyleSheet("background: transparent;")
        scroll_area.setWidget(scroll_content)
        self.__scroll_content_layout = QVBoxLayout(scroll_content)
        self.__scroll_content_layout.setAlignment(Qt.AlignmentFlag.AlignTop)

        display_panel_layout.addWidget(table_headings_container)
        display_panel_layout.addWidget(scroll_area)

        panel_layout.addWidget(control_panel, 1)
        panel_layout.addWidget(display_panel, 2)
    

    def initailise(self):
        self.__participant_rows = {}
        participant_list: list = self.__controller.get_participant_list()
        for participant in participant_list:
            id = participant.get_id()
            name = participant.get_name()
            row = TableRow(id, name)
            self.__participant_rows[name] = row
            self.__scroll_content_layout.addWidget(row)

            self.participant_count_label.setText(str(len(self.__controller.get_participant_list())))
    

    def _handle_add_participant_validation_result(self, result: str, participant) -> None:
        if result == "":
            self.__adding_participant_status_label.setText("Successfully added particpant")
            self.style_success_label(self.__adding_participant_status_label)

            index = self.__controller.get_participant_list().index(participant)
            id = participant.get_id()
            name = participant.get_name()
            row = TableRow(id, name)
            self.__participant_rows[name] = row
            self.__scroll_content_layout.insertWidget(index, row)

            self.new_participant_input.setText("")
            self.participant_count_label.setText(str(len(self.__controller.get_participant_list())))

        elif result != "":
            self.__adding_participant_status_label.setText(result)
            self.style_error_label(self.__adding_participant_status_label)

    def _handle_delete_participant_validation_result(self, result: str, name: str) -> None:
        if result == "":
            self.__delete_participant_status_label.setText("Successfully deleted particpant")
            self.style_success_label(self.__delete_participant_status_label)
            participant = self.__participant_rows.pop(name)
            self.__scroll_content_layout.removeWidget(participant)
            participant.setParent(None)
            participant.deleteLater()

            self.participant_to_delete_input.setText("")
            self.participant_count_label.setText(str(len(self.__controller.get_participant_list())))

        elif result != "":
            self.__delete_participant_status_label.setText(result)
            self.style_error_label(self.__delete_participant_status_label)
        
    def disable_participant_buttons(self):
        self.__submit_new_participant_button.setEnabled(False)
        self.__delete_participant_button.setEnabled(False)


class TableRow(QFrame, UIStyler):
    def __init__(self, id: int, name: str):
        super().__init__()
        self.__id = id
        self.__name = name

        self.setup_ui()

    def setup_ui(self):
        self.setFixedHeight(40)
        self.style_panel_3(self)

        layout = QHBoxLayout(self)
        layout.setAlignment(Qt.AlignmentFlag.AlignVCenter)

        id_label = QLabel(str(self.__id))
        id_label.setMinimumWidth(200)
        self.set_font_heading(id_label, "20px")
        name_label = QLabel(self.__name)
        name_label.setMaximumWidth(700)
        self.set_font_heading(name_label, "20px")

        seperator_line = QFrame()
        seperator_line.setFrameShape(QFrame.Shape.VLine)
        self.style_seperator_line(seperator_line, 25)

        layout.addWidget(id_label, 2)
        layout.addWidget(seperator_line)
        layout.addWidget(name_label, 8)