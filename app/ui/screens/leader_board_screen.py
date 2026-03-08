from PyQt6.QtWidgets import QWidget, QFrame, QVBoxLayout, QSizePolicy, QLabel, QTableView, QHBoxLayout, QHeaderView, QPushButton, QFileDialog
from PyQt6.QtCore import Qt
from utils.ui_styler import UIStyler

from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from controllers.leader_board_controller import LeaderBoardController


class LeaderBoardScreen(QWidget, UIStyler):
    def __init__(self, controller: "LeaderBoardController"):
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

        layout_backgound = QVBoxLayout(frame)
        layout_backgound.setContentsMargins(40,40,40,40)
        layout_backgound.setAlignment(Qt.AlignmentFlag.AlignHCenter)

        # Header container
        header_container = QWidget()
        header_container_layout = QHBoxLayout(header_container)
        header_container_layout.setAlignment(Qt.AlignmentFlag.AlignLeft)
        header_container_layout.setSpacing(0)
        rank_label = QLabel("     Rank")
        self.set_font_heading(rank_label, "20px")
        name_label = QLabel("          Name")
        self.set_font_heading(name_label, "20px")
        score_label = QLabel("                                   Score")
        self.set_font_heading(score_label, "20px")
        header_container_layout.addWidget(rank_label,1)
        header_container_layout.addWidget(name_label,8)
        header_container_layout.addWidget(score_label,3)

        layout_backgound.addWidget(header_container)
        table_background = QFrame()
        self.style_panel(table_background)
        layout_backgound.addWidget(table_background)

        # Leaderboard table
        table = QTableView()
        table.setModel(self.__controller.get_model())
        self.style_table(table)

        table.setSortingEnabled(False)
        table.verticalHeader().setVisible(False)
        table.horizontalHeader().setVisible(False)
        table.horizontalHeader().setStretchLastSection(False)
        table.verticalHeader().setDefaultSectionSize(44)
        table.setSelectionMode(QTableView.SelectionMode.NoSelection)
        table.setShowGrid(False)
        table.setFocusPolicy(Qt.FocusPolicy.NoFocus)
        table.setFrameShape(QFrame.Shape.NoFrame)

        header = table.horizontalHeader()

        header.setSectionResizeMode(QHeaderView.ResizeMode.Interactive)
        header.setStretchLastSection(False)

        table.setColumnWidth(0, 150)
        table.setColumnWidth(1, 1120)
        table.setColumnWidth(2, 200)

        layout = QVBoxLayout(table_background)
        layout.setContentsMargins(15,15,0,10)
        layout.addWidget(table)

        # Download CSV UI
        export_button = QPushButton("Export to CSV")
        export_button.setFixedSize(250,60)
        export_button.clicked.connect(self.export_csv)
        self.style_button(export_button, "20px")
        layout_backgound.addSpacing(20)
        layout_backgound.addWidget(export_button, alignment=Qt.AlignmentFlag.AlignHCenter)


    def export_csv(self):

        file_path = QFileDialog.getSaveFileName(
            self,
            "Save leanderboard",
            "",
            "CSV Files (*.csv)"
        )
        if not file_path:
            return
        self.__controller.export_to_csv(file_path)