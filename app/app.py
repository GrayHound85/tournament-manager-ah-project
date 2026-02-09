from PyQt6.QtWidgets import QApplication, QMainWindow
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
tournament_selector_screen = TournamentSelectorScreen(tournament_selector_controller=tournament_selector_controller)


window = QMainWindow()
window.setMinimumSize(600,400)
window.setWindowTitle("Tournament Manager")
window.show()


sys.exit(app.exec())