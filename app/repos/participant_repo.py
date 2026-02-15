import mysql.connector
from models.participant_model import Participant

from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from database.mysql_server_connection import Database

class ParticipantRepo:
    def __init__(self, db):
        self.__participant_list: list[Participant] = []
        self.__db: Database = db
        self.__id_counter = 0
    

    def add_participant(self, name) -> None:
        if self.__db == None:
            print("Tournament database has not been set.")
            return
        
        new_participant = Participant(self.__id_counter, name)
        self.__participant_list.append(new_participant)
        self.__id_counter += 1
        self.__db.execute(f"")