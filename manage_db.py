import sqlite3

from rich import print
import time
import logging

logging.basicConfig(level=logging.INFO)

DB_NAME = "BlaBl-App.db"




def init_db():
    try:
        sqliteConnection = sqlite3.connect(DB_NAME)
        sqlite_create_table_query = """CREATE TABLE message (
                                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                                    pic TEXT,
                                    nickname text NOT NULL,
                                    message text NOT NULL,
                                    time INTEGER NOT NULL);"""

        cursor = sqliteConnection.cursor()
        logging.info("Connected making table...")
        cursor.execute(sqlite_create_table_query)
        sqliteConnection.commit()
        logging.info("succes!")

        cursor.close()

    except sqlite3.Error as error:
        logging.error("Error while creating a sqlite table", error)
    finally:
        if sqliteConnection:
            sqliteConnection.close()

def add_message(nickname, pic, messageContent, time=int(time.time()*1000)):
    nb_row = 0
    try:
        sqliteConnection = sqlite3.connect(DB_NAME)
        cursor = sqliteConnection.cursor()
        logging.info("Connected adding message...")

        sqlite_select_Query = f"INSERT INTO message VALUES (null, '{pic}', '{nickname}','{messageContent}',{time});"
        cursor.execute(sqlite_select_Query)
        sqliteConnection.commit()
        nb_row = cursor.rowcount
        logging.info(f"added row {nb_row}",)
        cursor.close()
        

    except sqlite3.Error as error:
        logging.error("Error while adding message", error)
    finally:
        if sqliteConnection:
            sqliteConnection.close()

    return nb_row > 1 if True else False

def get_message(nb = 10, start=0):
    rows = []
    try:
        sqliteConnection = sqlite3.connect(DB_NAME)
        cursor = sqliteConnection.cursor()
        logging.info("Connected getting message...")

        sqlite_select_Query = f"SELECT * FROM message WHERE id > {start} ORDER BY time LIMIT {nb};"
        #sqlite_select_Query = f"SELECT name FROM sqlite_master WHERE type='table'"
        cursor.execute(sqlite_select_Query)
        rows = cursor.fetchall()
        logging.info(f"selected row {len(rows)}")
        cursor.close()
        

    except sqlite3.Error as error:
        logging.info("Error while getting message", error)
    finally:
        if sqliteConnection:
            sqliteConnection.close()

    return rows

if __name__ == "__main__":
    init_db()
    print(get_message())
    print(add_message("bob","","hi there"))
    print(get_message())
