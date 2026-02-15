from PyQt6.QtWidgets import QWidget, QVBoxLayout, QStackedWidget

class AppWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.stack = QStackedWidget()

        layout = QVBoxLayout(self)
        layout.addWidget(self.stack)
        layout.setContentsMargins(0,0,0,0)

    
    def add_screen(self, widget):
        self.stack.addWidget(widget)

    def show_screen(self, widget):
        self.stack.setCurrentWidget(widget)