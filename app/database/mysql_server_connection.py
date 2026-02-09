import mysql.connector

class Database:
    def __init__(self, host: str, username: str, password: str):
        self.__host = host
        self.__user = username
        self.__passwd = password
        self.__db = ""
    

    def validate_connection_credentials(self) -> bool:
        if self.__host and self.__user and self.__passwd and self.__db:
            return True
        else:
            return False
    

    def connect_to_server(self):
        print(mysql.connector.__version__)
        server_connection = mysql.connector.connect(
            host=self.__host,
            user=self.__user,
            passwd=self.__passwd
        )

        schema_cursor = server_connection.cursor()
        return server_connection, schema_cursor
    
    def connect_to_database(self, db_name: str):
        self.__db = db_name
        if self.validate_connection_credentials():
            db_connection = mysql.connector.connect(
                host=self.__host,
                user=self.__user,
                passwd=self.__passwd,
                db=self.__db
            )
            db_cursor = db_connection.cursor()
            return db_connection, db_cursor
        else:
            print("Can't connect to database: Some connection credentails are missing")
            return
