from PyQt6.QtWidgets import QApplication
from PyQt6.QtCore import QSize
import sys

from utils.app_window import AppWindow
from database.mysql_server_connection import Database

from repos.tournament_repo import TournamentRepo
from repos.participant_repo import ParticipantRepo
from repos.match_repo import MatchRepo

from controllers.tournament_selector_controller import TournamentSelectorController
from controllers.participant_manager_controller import ParticipantManagerController
from controllers.score_manager_controller import ScoreManagerController
from controllers.leader_board_controller import LeaderBoardController

from ui.screens.tournament_selector_screen import TournamentSelectorScreen
from ui.screens.page_changer_screen import PageChangerScreen
from ui.screens.participant_manager_screen import ParticipantManagerScreen
from ui.screens.score_manager_screen import ScoreManagerScreen
from ui.screens.leader_board_screen import LeaderBoardScreen


app = QApplication(sys.argv)
app_window = AppWindow()

# Database
db = Database(host="localhost", username="root", password="7632")

# Repos
tournament_repo = TournamentRepo(db=db)
participant_repo = ParticipantRepo(db=db)
match_repo = MatchRepo(db=db)

# Controllers
tournament_selector_controller = TournamentSelectorController(repo=tournament_repo)
particpant_manager_controller = ParticipantManagerController(participant_repo=participant_repo)
score_manager_controller = ScoreManagerController(participant_repo=participant_repo, match_repo=match_repo)
leader_board_controller = LeaderBoardController(participant_repo=participant_repo, match_repo=match_repo)

# Screens
tournament_selector_screen = TournamentSelectorScreen(controller=tournament_selector_controller)
participant_manager_screen = ParticipantManagerScreen(controller=particpant_manager_controller)
score_manager_screen = ScoreManagerScreen(controller=score_manager_controller)
leader_board_screen = LeaderBoardScreen(controller=leader_board_controller)
page_changer_screen = PageChangerScreen(screens= {
    "Participant Manager": participant_manager_screen,
    "Score Manager": score_manager_screen,
    "Leader Board": leader_board_screen
})


# App window + screen changing
app_window.add_screen(tournament_selector_screen)
app_window.add_screen(page_changer_screen)

tournament_selector_screen.openTournament.connect(lambda: app_window.show_screen(page_changer_screen))
tournament_selector_screen.openTournament.connect(participant_repo.initailise)
tournament_selector_screen.openTournament.connect(participant_manager_screen.initailise)
tournament_selector_screen.openTournament.connect(match_repo.initialise)


app_window.setMinimumSize(1000, 500)
app_window.resize(1600, 800)
app_window.setWindowTitle("Tournament Manager")
app_window.show()


sys.exit(app.exec())