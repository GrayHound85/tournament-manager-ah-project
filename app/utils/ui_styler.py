from PyQt6.QtWidgets import QWidget, QFrame, QPushButton, QLineEdit, QLabel, QScrollArea
from PyQt6.QtCore import Qt
from enum import Enum

class Colour(Enum):
    PRIMARY = "#275E8A"
    SECONDARY = "#E1C80B"
    BASE = "#DFDFDF"
    BASE2 = "#CECECE"
    Base3 = "#A5A5A5"
    OUTLINE = "#ADADAD"
    FONT = "#535353"
    FONT_INVERSE = "#EAEAEA"
    ERROR = "#F21515"

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
        
    def style_button(self, button: QPushButton, size: str = "12px") -> None:
        button.setStyleSheet(f"""
            QPushButton {{
                background-color: {Colour.PRIMARY.value};
                color: {Colour.FONT_INVERSE.value};
                padding: {Size.PADDING.value};
                border-radius: {Size.BORDER_RADIUS.value};
                font-size: {size};
            }}
        """)
    
    def style_button_2(self, button: QPushButton, size: str = "12px") -> None:
        button.setStyleSheet(f"""
            QPushButton {{
                background-color: {Colour.Base3.value};
                color: {Colour.FONT_INVERSE.value};
                padding: {Size.PADDING.value};
                border-radius: {Size.BORDER_RADIUS.value};
                font-size: {size};
            }}
        """)
    
    def set_screen_margin(self, widget) -> None:
        widget.setContentsMargins(20, 20, 20, 20)
    

    def set_font_heading(self, widget, size: str = "50px"):
        widget.setStyleSheet(f"""
            * {{
                color: {Colour.FONT.value};
                font-size: {size};
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
    
    def style_line_edit(self, widget: QLineEdit, size: str = "10px"):
        widget.setStyleSheet(f"""
            QLineEdit {{
                background-color: {Colour.Base3.value};
                color: {Colour.FONT_INVERSE.value};
                padding: {Size.PADDING.value};
                border-radius: {Size.BORDER_RADIUS.value};
                font-size: {size};
            }}
        """)
    
    def style_error_label(self, label: QLabel, size: str = "20px"):
        label.setStyleSheet(f"""
            QLabel {{
                color: {Colour.ERROR.value};
                font-size: {size};
            }}
        """) 
    
    def style_scroll_area(self, scroll_area: QScrollArea):
        scroll_area.setStyleSheet(f"""
            QScrollArea {{
                border: {Size.LINE_THICKNESS.value} solid {Colour.OUTLINE.value};
                border-radius: {Size.BORDER_RADIUS.value};
                background: transparent;
            }}
        """) 