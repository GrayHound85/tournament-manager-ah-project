import mysql.connector
from models.participant_model import Participant
from utils.standard_algorithms import StandardAlgorithms

from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from database.mysql_server_connection import Database

class ParticipantRepo:
    def __init__(self, db):
        self.__participant_list: list[Participant] = []
        self.__db: Database = db
        self.__id_counter = 0

    
    def confirm_database_connection(self) -> bool:
        if self.__db == None:
            print("Tournament database has not been set.")
            return False
        return True
    

    def add_participant(self, name: str) -> None:
        if not self.confirm_database_connection():
            return
        
        new_participant = Participant(self.__id_counter, name)
        self.__participant_list.append(new_participant)
    
        self.__db.get_db_cursor().execute(f"""
            INSERT INTO Participants
            VALUES ({self.__id_counter}, {name});
        """)
        self.__db.get_db_connection().commit()
        self.__id_counter += 1


    def remove_participant(self, name: str) -> None:
        if not self.confirm_database_connection():
            return
        
        self.__db.get_db_cursor().execute(f"""
            DELETE FROM Participants WHERE participantName = {name};
        """)
        self.__db.get_db_connection().commit()
