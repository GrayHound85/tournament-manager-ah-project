import mysql.connector
from models.match_model import Match
from utils.standard_algorithms import StandardAlgorithms

from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from database.mysql_server_connection import Database

class MatchRepo:
    def __init__(self, db):
        self.__match_list: list[Match] = []
        self.__db: Database = db
        self.__id_counter = 0
        self.__matches_generated = False

    def initialise(self):
        if not self.confirm_database_connection():
            return
        self.__db.get_db_cursor().execute("""
            SELECT *
            FROM MatchScore
        """)

        match_lookup = {}

        result = self.__db.get_db_cursor().fetchall()
        for participant_id, match_id, participant_score, round in result:
            #print(f"participant id: {participant_id}, match_id: {match_id}, participant score: {participant_score}, round: {round}")
            if match_id not in match_lookup:
                match_lookup[match_id] = Match(match_id, [participant_id], round)
            else:
                match_lookup[match_id].add_participant(participant_id)
        
        self.__match_list = list(match_lookup.values())
        if self.__match_list:
            self.__matches_generated = True
            print("Matches have been generated")
        
        self.__match_list = StandardAlgorithms.insertion_sort(self.__match_list, "id")
    
 

    def create_match(self, round_id: int, players: list):
        participant_ids = [player.get_id() for player in players]
        match = Match(self.__id_counter, participant_ids, round_id)
        self.__match_list.append(match)

        for player in players:
            self.__db.get_db_cursor().execute(f"""
                INSERT INTO MatchScore(participantID, matchID, matchScore, roundNum)
                VALUES({player.get_id()}, {self.__id_counter}, -1, {round_id})
            """)
        
        self.__db.get_db_connection().commit()
        self.__id_counter += 1


    def confirm_database_connection(self) -> bool:
        if self.__db == None:
            print("Tournament database has not been set.")
            return False
        return True
    

    def fixtures_generated(self) -> bool:
        return self.__matches_generated
    

    def get_matches(self):
        return self.__match_list