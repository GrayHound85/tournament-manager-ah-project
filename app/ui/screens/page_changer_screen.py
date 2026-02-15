from PyQt6.QtWidgets import QWidget, QTabBar, QVBoxLayout, QTabWidget

from utils.ui_styler import UIStyler

class PageChangerScreen(QWidget, UIStyler):
    def __init__(self, screens: dict[str: QWidget]):
        super().__init__()
        self.__screens = screens
        self.setup_ui()


    def setup_ui(self):
        tab_container = QTabWidget()

        layout = QVBoxLayout(self)
        layout.addWidget(tab_container)

        for name, screen in self.__screens.items():
            tab_container.addTab(screen, name)