import mysql.connector
from app.models.participant_model import Participant

class ParticipantRepo:
    def __init__(self):
        self.__participant_list = []
        self.__db = None
        self.__id_counter = 0
    

    def add_participant(self, name):
        if self.__db == None:
            print("Tournament database has not been set.")
            return
        
        new_participant = Participant(self.__id_counter, name)
        self.__participant_list.append(new_participant)
        self.__id_counter += 1
        self.__db.execute(f"")