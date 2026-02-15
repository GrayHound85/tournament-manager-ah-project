import mysql.connector
from models.match_model import Match

from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from database.mysql_server_connection import Database

class MatchRepo:
    def __init__(self, db):
        self.__match_list: list[Match] = []
        self.__db: Database = db
        self.__id_counter = 0