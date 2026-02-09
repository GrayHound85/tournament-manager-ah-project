from PyQt6.QtWidgets import QWidget
from PyQt6.QtCore import Qt
from enum import Enum

class Colour(Enum):
    PRIMARY = "#FFFFFF"
    SECONDARY = "#FFFFFF"
    BASE = "#FFFFFF"
    BASE2 = "#FFFFFF"
    OUTLINE = "#FFFFFF"
    FONT = "#FFFFFF"

class Size(Enum):
    PADDING = "8px"
    BORDER_RADIUS = "6px"

class UIStyler(QWidget):
    def __init__(self):
        super().__init__()
    

    def style_primary_frame(frame):
        frame.setStyleSheet(f"""
            QPushButton {{
                background-color: {Colour.BASE};
                padding: {Size.PADDING};
                border-radius: {Size.BORDER_RADIUS};
            }}
        """)



    def style_button_default(button):
        button.setStyleSheet(f"""
            QPushButton {{
                background-color: {Colour.BASE};
                color: {Colour.FONT};
                padding: {Size.PADDING};
                border-radius: {Size.BORDER_RADIUS};
            }}
        """)

