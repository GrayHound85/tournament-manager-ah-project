from PyQt6.QtWidgets import QWidget, QFrame, QPushButton
from PyQt6.QtCore import Qt
from enum import Enum

class Colour(Enum):
    PRIMARY = "#275E8A"
    SECONDARY = "#E1C80B"
    BASE = "#DFDFDF"
    BASE2 = "#CECECE"
    OUTLINE = "#FFFFFF"
    FONT = "#535353"
    FONT_INVERSE = "#EAEAEA"

class Size(Enum):
    PADDING = "8px"
    BORDER_RADIUS = "20px"
    LINE_THICKNESS = 4

class UIStyler():   
    def style_primary_frame(self, frame: QFrame) -> None:
        frame.setStyleSheet(f"""
            QFrame {{
                background-color: {Colour.BASE.value};
            }}
        """)
        
    def style_button_default(self, button: QPushButton, size: str = "12px") -> None:
        button.setStyleSheet(f"""
            QPushButton {{
                background-color: {Colour.PRIMARY.value};
                color: {Colour.FONT_INVERSE.value};
                padding: {Size.PADDING.value};
                border-radius: {Size.BORDER_RADIUS.value};
                font-size: {size};
            }}
        """)
    
    def set_screen_margin(self, widget) -> None:
        widget.setContentsMargins(20, 20, 20, 20)
    

    def set_font_heading(self, widget):
        widget.setStyleSheet(f"""
            * {{
                color: {Colour.FONT.value};
                font-size: 50px;
            }}
        """)
    
    def style_seperator_line(self, frame: QFrame, length: int) -> None:
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

    def style_panel(self, frame: QFrame) -> None:
        frame.setStyleSheet(f"""
            QFrame {{
                background-color: {Colour.BASE2.value};
                border-radius: {Size.BORDER_RADIUS.value};
            }}
        """)
    