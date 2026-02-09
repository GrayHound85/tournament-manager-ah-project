from PyQt6.QtWidgets import QWidget
from PyQt6.QtCore import Qt
from enum import Enum

class Colour(Enum):
    PRIMARY = "#FFFFFF"
    SECONDARY = "#FFFFFF"
    BASE = "#353535"
    BASE2 = "#FFFFFF"
    OUTLINE = "#FFFFFF"
    FONT = "#FFFFFF"

class Size(Enum):
    PADDING = "8px"
    BORDER_RADIUS = "6px"

class UIStyler():
    def style_primary_frame(self, frame):
        frame.setStyleSheet(f"""
            QFrame {{
                background-color: {Colour.BASE.value};
            }}
        """)
        
    def style_button_default(self, button):
        button.setStyleSheet(f"""
            QPushButton {{
                background-color: {Colour.BASE.value};
                color: {Colour.FONT.value};
                padding: {Size.PADDING.value};
                border-radius: {Size.BORDER_RADIUS.value};
            }}
        """)
    
    def set_screen_margin(self, widget):
        widget.setContentsMargins(20, 20, 20, 20)
    