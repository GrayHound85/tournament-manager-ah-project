import mysql.connector

class TournamentRepo:
    def __init__(self, schema_cursor):
        self.__schema_cur = schema_cursor
    

    def get_databases(self) -> list[tuple]:
        self.__schema_cur.execute("SHOW DATABASES;")
        result = self.__schema_cur.fetchall()
        return result

    def add_tournament(self, name):
        print(f"Adding tournament... {name}")