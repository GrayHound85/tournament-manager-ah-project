from PyQt6.QtWidgets import QApplication
from PyQt6.QtCore import QSize
import sys

from utils.app_window import AppWindow
from database.mysql_server_connection import Database

from repos.tournament_repo import TournamentRepo

from controllers.tournament_selector_controller import TournamentSelectorController

from ui.screens.tournament_selector_screen import TournamentSelectorScreen
from ui.screens.page_changer_screen import PageChangerScreen


app = QApplication(sys.argv)
app_window = AppWindow()

# Database
db = Database(host="localhost", username="root", password="7632")

# Repos
tournament_repo = TournamentRepo(db=db)

# Controllers
tournament_selector_controller = TournamentSelectorController(repo=tournament_repo)

# Screens
tournament_selector_screen = TournamentSelectorScreen(controller=tournament_selector_controller)
page_changer_screen = PageChangerScreen()


# App window + screen changing
app_window.add_screen(tournament_selector_screen)
app_window.add_screen(page_changer_screen)

tournament_selector_screen.openTournament.connect(lambda: app_window.show_screen(page_changer_screen))


app_window.setMinimumSize(1000, 500)
app_window.resize(1600, 800)
app_window.setWindowTitle("Tournament Manager")
app_window.show()


sys.exit(app.exec())