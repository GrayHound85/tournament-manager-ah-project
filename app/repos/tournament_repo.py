import mysql.connector

class TournamentRepo:
    def __init__(self, schema_cursor):
        self.__schema_cur = schema_cursor
    

    def databases_list(self):
        self.__schema_cur.execute("SHOW DATABASES;")
        result = self.__schema_cur.fetchall()
        db_names = [db[0] for db in result]
        return db_names

    