from PyQt6.QtCore import QObject, pyqtSignal

class PageChangerController(QObject):
    def __init__(self):
        super().__init__()