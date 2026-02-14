import mysql.connector

class Database:
    def __init__(self, host: str, username: str, password: str):
        self.__host = host
        self.__user = username
        self.__passwd = password
        self.__db = ""

        self.__server_connection, self.__schema_cursor = self.connect_to_server()
        
        self.__db_connection = None
        self.__db_cursor = None
    

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
            self.__db_connection = db_connection
            self.__db_cursor = db_cursor
            print(f"Connected to database: {db_name}")

    def get_db_cursor(self):
        return self.__db_cursor
    
    def get_schema_cursor(self):
        return self.__schema_cursor