from PyQt6.QtWidgets import QWidget, QFrame, QVBoxLayout, QSizePolicy, QLabel, QStackedWidget, QHBoxLayout, QSpinBox, QPushButton
from PyQt6.QtCore import Qt
from utils.ui_styler import UIStyler

from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from controllers.score_manager_controller import ScoreManagerController


class ScoreManagerScreen(QWidget, UIStyler):
    def __init__(self, controller: "ScoreManagerController"):
        super().__init__()
        self.__controller = controller
        self.__match_display_index = 0
        self.__rows_displayed: dict = {}
        self.setup_ui()
    

    def initailise(self) -> None:
        if not self.__controller.fixtures_generated():
            return
        
        self.__widget_stacker.setCurrentIndex(1)
        self.display_match(0)
    
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
        layout = QVBoxLayout(frame)
        layout.setContentsMargins(30,30,30,0)

        self.__widget_stacker = QStackedWidget()
        layout.addWidget(self.__widget_stacker)

        # Generate fixtuers panel
        panel_1_container = QWidget()
        panel_1_layout = QVBoxLayout(panel_1_container)
        panel_1_layout.setAlignment(Qt.AlignmentFlag.AlignHCenter)

        # Holds the panel for entering how many rounds are to be played
        input_container = QFrame()
        input_container.setFixedSize(500,150)
        self.style_panel(input_container)
        input_container_layout = QHBoxLayout(input_container)
        input_container_layout.setContentsMargins(40,40,40,40)

        input_label = QLabel("Number of rounds")
        self.set_font_heading(input_label, "20px")
        rounds_input_spinbox = QSpinBox()
        rounds_input_spinbox.setRange(1,128)
        rounds_input_spinbox.setSingleStep(1)
        self.style_spinbox(rounds_input_spinbox)
        input_container_layout.addWidget(input_label)
        input_container_layout.addWidget(rounds_input_spinbox)

        generate_fixtures_button = QPushButton("Generate fixtures")
        generate_fixtures_button.setFixedSize(300,60)
        generate_fixtures_button.clicked.connect(lambda: self.__controller.request_fixture_generation(rounds_input_spinbox.value()))
        self.__controller.fixturesGenerated.connect(lambda: (self.__widget_stacker.setCurrentIndex(1), self.display_match(0)))
        self.style_button(generate_fixtures_button, "20px")

        panel_1_layout.addWidget(input_container)
        panel_1_layout.addSpacing(300)
        panel_1_layout.addWidget(generate_fixtures_button, alignment=Qt.AlignmentFlag.AlignHCenter)

        # Holds the panel where the user can input score for each match (only appears after fixtures have been generated)
        panel_2_container = QWidget()
        panel_2_layout = QVBoxLayout(panel_2_container)

        # Subpanel for inputing score
        score_input_panel = QFrame()
        self.style_panel(score_input_panel)
        self.__score_input_layout = QVBoxLayout(score_input_panel)
        self.__score_input_layout.setContentsMargins(80,60,80,40)
        self.__score_input_layout.setSpacing(40)
        self.__stretch_item = None

        # Header container
        self.__header_container = QWidget()
        self.__header_container.setFixedHeight(20)
        header_layout = QHBoxLayout(self.__header_container)
        header_layout.setContentsMargins(0,0,0,0)
        name_heading_label = QLabel("  Name")
        self.set_font_heading(name_heading_label, "20px")
        score_input_heading_label = QLabel("Score")
        self.set_font_heading(score_input_heading_label, "20px")

        header_layout.addWidget(name_heading_label, 8)
        header_layout.addWidget(score_input_heading_label, 2)
        
        self.__score_input_layout.addWidget(self.__header_container)

        # Subpanel for changing match to display
        change_match_panel = QWidget()
        change_match_layout = QHBoxLayout(change_match_panel)
        previous_match_button = QPushButton("Previous")
        previous_match_button.clicked.connect(lambda: self.display_match(-1))
        previous_match_button.setFixedSize(200,60)
        self.style_button(previous_match_button, "20px")
        next_match_button = QPushButton("Next + Submit")
        next_match_button.clicked.connect(lambda: (self.submit_scores(), self.display_match(1)))
        next_match_button.setFixedSize(200,60)
        self.style_button(next_match_button, "20px")

        match_id_container = QWidget()
        match_id_container.setFixedWidth(300)
        match_id_container_layout = QVBoxLayout(match_id_container)
        match_id_container_layout.setAlignment(Qt.AlignmentFlag.AlignHCenter)
        match_id_static_label = QLabel("Match ID")
        self.set_font_heading(match_id_static_label, "20px")
        self.__match_id_label = QLabel("1024")
        self.style_counter_label(self.__match_id_label, "30px")
        match_id_container_layout.addWidget(match_id_static_label)
        match_id_container_layout.addWidget(self.__match_id_label)

        change_match_layout.addStretch()
        change_match_layout.addWidget(previous_match_button)
        change_match_layout.addWidget(match_id_container)
        change_match_layout.addWidget(next_match_button)
        change_match_layout.addStretch()


        panel_2_layout.addWidget(score_input_panel,4)
        panel_2_layout.addWidget(change_match_panel,1)


        self.__widget_stacker.addWidget(panel_1_container)
        self.__widget_stacker.addWidget(panel_2_container)

    
    def display_match(self, next: int) -> None:
        self.__rows_displayed.clear()

        if next == 1 and len(self.__controller.get_matches())-1 > self.__match_display_index:
            self.__match_display_index += next

        if next == -1 and self.__match_display_index > 0:
            self.__match_display_index += next
        
        while self.__score_input_layout.count() > 1:
            item = self.__score_input_layout.takeAt(1)
            widget = item.widget()
            if widget is not None:
                widget.deleteLater()
        
        if self.__stretch_item is not None:
            self.__score_input_layout.removeItem(self.__stretch_item)

        self.__score_input_layout.addWidget(self.__header_container)
        match = self.__controller.get_match(self.__match_display_index)
        for participant in match.get_participants():
            name = self.__controller.get_participant_name(participant)
            score = self.__controller.get_participant_score(self.__match_display_index, participant)
            row = ScoreInputRow(name, score)
            self.__rows_displayed[participant] = row
            self.__score_input_layout.addWidget(row)
        self.__match_id_label.setText(str(match.get_id()))
        self.__stretch_item = self.__score_input_layout.addStretch()
    

    def submit_scores(self):
        participant_scores = {}
        for participant_id in self.__rows_displayed:
            participant_scores[participant_id] = self.__rows_displayed[participant_id].get_score()
        self.__controller.set_match_scores(self.__match_display_index, participant_scores)



class ScoreInputRow(QFrame, UIStyler):
    def __init__(self, name: str, score: int):
        super().__init__()
        self.__name = name
        self.__score: int = score
        print(self.__score)
        self.setup_ui()

    
    def setup_ui(self) -> None:
        self.style_panel_3(self)
        self.setFixedHeight(60)
        layout = QHBoxLayout(self)

        name_label = QLabel(self.__name)
        self.set_font_heading(name_label, "20px")
        seperator_line = QFrame()
        seperator_line.setFrameShape(QFrame.Shape.VLine)
        self.style_seperator_line(seperator_line, 40)
        self.__score_input_field = QSpinBox()
        self.__score_input_field.setValue(int(self.__score))
        self.__score_input_field.setRange(0, 1024)
        self.__score_input_field.setSingleStep(1)
        self.style_spinbox(self.__score_input_field)

        layout.addWidget(name_label,8)
        layout.addWidget(seperator_line)
        layout.addWidget(self.__score_input_field,2)
    
    def get_score(self) -> int:
        return self.__score_input_field.value()
