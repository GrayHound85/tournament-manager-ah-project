import mysql.connector

from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from database.mysql_server_connection import Database

class TournamentRepo:
    def __init__(self, db):
        self.__db: Database = db
    

    def get_databases(self) -> list[tuple]:
        self.__db.get_schema_cursor().execute("SHOW DATABASES;")
        result = self.__db.get_schema_cursor().fetchall()
        return result

    def add_tournament(self, name):
        self.__db.get_schema_cursor().execute(f"CREATE DATABASE {name};")
        self.__db.connect_to_database(name)
    
    def setup_database(self):
        self.__db.get_db_cursor().execute(f"""
            CREATE TABLE Participants(
                participantID INT PRIMARY KEY NOT NULL,
                participantName VARCHAR(128) NOT NULL
            );
        """)

        self.__db.get_db_cursor().execute(f"""
            CREATE TABLE MatchScore(
                participantID INT NOT NULL,
                matchID INT NOT NULL,
                matchScore FLOAT NOT NULL,
                roundNum INT NOT NULL,
                FOREIGN KEY (participantID) REFERENCES Participants(participantID)
            );
        """)
    
    def delete_tournament(self, name):
        self.__db.get_schema_cursor().execute(f"DROP DATABASE {name};")
    
    def open_tournament(self, name):
        self.__db.connect_to_database(name)