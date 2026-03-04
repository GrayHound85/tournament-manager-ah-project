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
    

    # Runs once on app start up to load all data from database and populate the array of Participant objects
    def initailise(self):
        if not self.confirm_database_connection():
            return
        self.__db.get_db_cursor().execute("""
            SELECT *
            FROM Participants;        
        """)
        result = self.__db.get_db_cursor().fetchall()
        for item in result:
            id: int = item[0]
            name: str = item[1]
            new_participant = Participant(id, name)
            self.__participant_list.append(new_participant)

        # Set __id_counter to the max id found
        self.__id_counter = StandardAlgorithms.find_max(self.__participant_list, "id") + 1
        self.__participant_list = StandardAlgorithms.insertion_sort(self.__participant_list, "name")

    
    def confirm_database_connection(self) -> bool:
        if self.__db == None:
            print("Tournament database has not been set.")
            return False
        return True
    

    def add_participant(self, name: str) -> Participant:
        if not self.confirm_database_connection():
            return
        
        id = self.__id_counter
        self.__id_counter += 1

        new_participant = Participant(id, name)
        self.__participant_list.append(new_participant)
    
        self.__db.get_db_cursor().execute(f"""
            INSERT INTO Participants(participantID, participantName)
            VALUES ({id}, "{name}");
        """)
        self.__db.get_db_connection().commit()
        self.__participant_list = StandardAlgorithms.insertion_sort(self.__participant_list, "name")

        return new_participant


    def delete_participant(self, index: int) -> None:
        if not self.confirm_database_connection():
            return
        
        id = self.__participant_list[index].get_id()
        
        print(f"deleting {id}")
        
        self.__db.get_db_cursor().execute(f"""
            DELETE FROM Participants WHERE participantID = %s;
        """, (id,))

        self.__db.get_db_connection().commit()
        self.__participant_list.pop(index)
    

    def get_participant_list(self):
        return self.__participant_list
    

