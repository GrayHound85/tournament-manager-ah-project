from PyQt6.QtWidgets import QWidget, QFrame, QPushButton, QLineEdit, QLabel, QScrollArea, QTableWidget
from PyQt6.QtCore import Qt
from enum import Enum

class Colour(Enum):
    PRIMARY = "#275E8A"
    SECONDARY = "#E1C80B"
    BASE = "#DFDFDF"
    BASE2 = "#CECECE"
    BASE3 = "#A5A5A5"
    OUTLINE = "#ADADAD"
    FONT = "#535353"
    FONT_INVERSE = "#EAEAEA"
    ERROR = "#F21515"
    SUCCESS = "#11CF00"

class Size(Enum):
    PADDING = "8px"
    BORDER_RADIUS = "20px"
    BORDER_INNER_RADIUS = "12px"
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
                background: transparent;
                color: {Colour.FONT_INVERSE.value};
                border-radius: {Size.BORDER_INNER_RADIUS.value};
                font-size: {size};
                text-align: left;
                padding: 16px
            }}
        """)
    
    def set_screen_margin(self, widget) -> None:
        widget.setContentsMargins(20, 20, 20, 20)
    

    def set_font_heading(self, widget, size: str = "50px"):
        widget.setStyleSheet(f"""
            * {{
                color: {Colour.FONT.value};
                font-size: {size};
                text-align: center;
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
    
    def style_panel_2(self, frame: QFrame) -> None:
        frame.setStyleSheet(f"""
            QFrame {{
                background-color: {Colour.BASE3.value};
                border-radius: {Size.BORDER_INNER_RADIUS.value};
            }}
        """)

    def style_panel_3(self, frame: QFrame) -> None:
        frame.setStyleSheet(f"""
            QFrame {{
                background-color: {Colour.BASE.value};
                border-radius: {Size.BORDER_INNER_RADIUS.value};
            }}
        """)
    
    def style_line_edit(self, widget: QLineEdit, size: str = "10px"):
        widget.setStyleSheet(f"""
            QLineEdit {{
                background-color: {Colour.BASE3.value};
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

    def style_success_label(self, label: QLabel, size: str = "20px"):
        label.setStyleSheet(f"""
            QLabel {{
                color: {Colour.SUCCESS.value};
                font-size: {size};
            }}
        """) 
    
    def style_scroll_area(self, scroll_area: QScrollArea):
        scroll_area.setStyleSheet(f"""
            QScrollArea {{
                border: {Size.LINE_THICKNESS.value} solid {Colour.OUTLINE.value};
                border-radius: {Size.BORDER_RADIUS.value};
                background: transparent;
                margin: 0px 0px 0px 0px;
            }}
        """)

        scroll_area.verticalScrollBar().setStyleSheet(f"""
            QScrollBar:vertical {{
                width: 20px;
                margin: 5px 10px 5px 0px;
                background: transparent;
                border: none;
            }}

            QScrollBar::handle:vertical {{
                background: rgba(150,150,150,180);
                border-radius: 5px;
                min-height: 30px;
            }}

            QScrollBar::handle:vertical:hover {{
                background: rgba(120,120,120,200);
            }}

            QScrollBar::handle:vertical:pressed {{
                background: rgba(100,100,100,220);
            }}

            QScrollBar::add-line:vertical,
            QScrollBar::sub-line:vertical {{
                height: 0px;
            }}

            QScrollBar::add-page:vertical,
            QScrollBar::sub-page:vertical {{
                background: none;
            }}
        """)

    def set_background_tranparent(self, widget):
        widget.setStyleSheet(f"""
            * {{
                background: transparent;
            }}
        """)
    
    def style_tab_container(self, tab_container: QTableWidget):
        tab_container.setStyleSheet(f"""
            QTabBar::tab {{
                background: {Colour.BASE2.value};
                color: {Colour.FONT.value};
                padding: 8px 20px;
                border-top-left-radius: {Size.BORDER_INNER_RADIUS.value};
                border-top-right-radius: {Size.BORDER_INNER_RADIUS.value};
                position: relative;
                top: 6px;
                border: none;
            }}

            QTabBar::tab:selected {{
                background: {Colour.BASE.value};
                font-size: 16px;
                top: 0px;
            }}

            QTabBar::tab:hover {{
                background: {Colour.BASE3.value};
            }}

            QTabWidget::pane {{
                border: none;
                margin: 0px;
                padding: 0px;
            }}

            QTabWidget {{
                border: none;
            }}
        """)
    
    def style_counter_label(self, label: QLabel, size: str):
        label.setStyleSheet(f"""
            * {{
                background: {Colour.BASE.value};
                border-radius: {Size.BORDER_INNER_RADIUS.value};
                color: {Colour.FONT.value};
                font-size: {size};
                text-align: center;
            }}
        """)

    def style_spinbox(self, spinbox):
        spinbox.setStyleSheet(f"""
            QSpinBox {{
                background-color: {Colour.BASE3.value};
                border: 2px solid {Colour.BASE3.value};
                border-radius: {Size.BORDER_INNER_RADIUS.value};
                padding: 4px 8px;
                color: {Colour.FONT_INVERSE.value};
                font-size: 20px;
            }}

            QSpinBox:hover {{
                border: 2px solid {Colour.PRIMARY.value};
            }}

            QSpinBox::up-button, QSpinBox::down-button {{
                width: 0px;
                height: 0px;
                border: none;
            }}

            QSpinBox::up-arrow, QSpinBox::down-arrow {{
                image: none;
            }}
        """)