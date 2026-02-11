
# Enables type hinting for classes passed in.
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from repos.tournament_repo import TournamentRepo


class TournamentSelectorController:
    def __init__(self, tournament_repo):
        self.__tournament_repo: "TournamentRepo" = tournament_repo

    
    def get_all_tournament(self) -> list[str]:
        result = self.__tournament_repo.get_databases()
        db_names = [db[0] for db in result]
        return db_names