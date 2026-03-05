from PyQt6.QtWidgets import QWidget, QFrame, QVBoxLayout, QSizePolicy, QLabel, QTableView, QHeaderView
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

        table_background = QFrame()
        self.style_panel(table_background)
        layout_backgound.addWidget(table_background)

        table = QTableView()
        table.setModel(self.__controller.get_model())
        self.style_table(table)

        table.setSortingEnabled(False)
        table.verticalHeader().setVisible(False)
        table.horizontalHeader().setStretchLastSection(True)
        table.verticalHeader().setDefaultSectionSize(44)
        table.setSelectionMode(QTableView.SelectionMode.NoSelection)

        width = table.viewport().width()
        table.setColumnWidth(0, int(width * 0.15))
        table.setColumnWidth(1, int(width * 0.70))
        table.setColumnWidth(2, int(width * 0.15))

        layout = QVBoxLayout(table_background)
        layout.addWidget(table)


