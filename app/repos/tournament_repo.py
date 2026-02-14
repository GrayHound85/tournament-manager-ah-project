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
    
    def delete_tournament(self, name):
        self.__db.get_schema_cursor().execute(f"DROP DATABASE {name};")
    
    def open_tournament(self, name):
        self.__db.connect_to_database(name)