from PyQt6.QtWidgets import QApplication
from PyQt6.QtCore import QSize
import sys

from database.mysql_server_connection import Database
from repos.tournament_repo import TournamentRepo
from controllers.tournament_selector_controller import TournamentSelectorController
from ui.screens.tournament_selector_screen import TournamentSelectorScreen


app = QApplication(sys.argv)

db = Database(host="localhost", username="root", password="7632")
server_connection, schema_cursor = db.connect_to_server()

tournament_repo = TournamentRepo(schema_cursor=schema_cursor)

tournament_selector_controller = TournamentSelectorController(tournament_repo=tournament_repo)

tournament_selector_screen = TournamentSelectorScreen(controller=tournament_selector_controller)


window = tournament_selector_screen
window.setMinimumSize(1000, 500)
window.resize(1600, 800)
window.setWindowTitle("Tournament Manager")
window.show()


sys.exit(app.exec())