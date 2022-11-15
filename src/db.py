import sqlite3


def connect_db(db_source):
    try:
        con = sqlite3.connect(db_source)
        return con
    except Exception as e:
        print(e)


def run_migration():
    pass
