from PyQt6.QtWidgets import QWidget
from enum import Enum

class Colour(Enum):
    PRIMARY = "#FFFFFF"
    SECONDARY = "#FFFFFF"
    BASE = "#FFFFFF"
    BASE2 = "#FFFFFF"
    OUTLINE = "#FFFFFF"

class UIStyler(QWidget):
    def __init__(self):
        super().__init__()


    def style_button_default(button):
        button.set

