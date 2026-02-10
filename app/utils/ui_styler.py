from PyQt6.QtWidgets import QWidget, QFrame
from PyQt6.QtCore import Qt
from enum import Enum

class Colour(Enum):
    PRIMARY = "#254E70"
    SECONDARY = "#E1C80B"
    BASE = "#DFDFDF"
    BASE2 = "#CECECE"
    OUTLINE = "#FFFFFF"
    FONT = "#535353"

class Size(Enum):
    PADDING = "8px"
    BORDER_RADIUS = "20px"
    LINE_THICKNESS = 4

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
    

    def set_font_heading(self, widget):
        widget.setStyleSheet(f"""
            * {{
                color: {Colour.FONT.value};
                font-size: 50px;
            }}
        """)
    
    def style_seperator_line(self, frame, length):
        frame.setStyleSheet(f"""
            QFrame {{
                background-color: {Colour.SECONDARY.value};
                color: {Colour.SECONDARY.value};
            }}
        """)   
    
        if frame.frameShape() == QFrame.Shape.HLine:
            frame.setFixedHeight(Size.LINE_THICKNESS.value)
            frame.setFixedWidth(length)
        elif frame.frameShape() == QFrame.Shape.VLine:
            frame.setFixedHeight(length)
            frame.setFixedWidth(Size.LINE_THICKNESS.value)

    def style_panel(self, frame):
        frame.setStyleSheet(f"""
            QFrame {{
                background-color: {Colour.BASE2.value};
                border-radius: {Size.BORDER_RADIUS.value};
            }}
        """)