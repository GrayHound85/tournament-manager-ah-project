from app.database.mysql_server_connection import Database
from app.repos.tournament_repo import TournamentRepo

def connectivity_test():
    db = Database(host="localhost", username="root", password="7632")
    print(db.connect_to_server())


def show_databases_test():
    db = Database(host="localhost", username="root", password="7632")
    server_connection, schema_cursor = db.connect_to_server()
    tournament_repo = TournamentRepo(schema_cursor=schema_cursor)
    database_list = tournament_repo.databases_list()
    print(database_list)




def main():
    show_databases_test()

main()