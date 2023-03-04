import logging
import sqlite3
import time

from rich import print

logging.basicConfig(level=logging.INFO)

DB_NAME = "BlaBl-App.db"


def drop_db():
    try:
        sqlite_connection, cursor = init_connection()
        sqlite_create_table_query = "DROP TABLE message"
        logging.info("Connected dropping table...")
        cursor.execute(sqlite_create_table_query)
        sqlite_connection.commit()
        logging.info("succes!")

        cursor.close()

    except sqlite3.Error as error:
        logging.error("Error while dropping table", error)
    finally:
        if sqlite_connection:
            sqlite_connection.close()


def init_db():
    drop_db()
    try:
        sqlite_create_table_query = """CREATE TABLE message (
                                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                                    pic TEXT,
                                    nickname TEXT NOT NULL,
                                    message TEXT NOT NULL,
                                    forum INTEGER NOT NULL,
                                    time INTEGER NOT NULL);"""

        sqlite_connection, cursor = init_connection()
        logging.info("Connected making table...")
        cursor.execute(sqlite_create_table_query)
        sqlite_connection.commit()
        logging.info("succes!")

        cursor.close()

    except sqlite3.Error as error:
        logging.error("Error while creating a sqlite table", error)
    finally:
        if sqlite_connection:
            sqlite_connection.close()


def insert_message(nickname, pic, message_content, forum, time=int(time.time() * 1000)):
    nb_row = 0
    try:
        message_content = message_content.replace('\'', "")
        sqlite_connection, cursor = init_connection()
        logging.info("Connected adding message...")
        print(forum)
        sqlite_select_query = f"INSERT INTO message VALUES (null, '{pic}', '{nickname}','{message_content}', {forum},{time});"
        cursor.execute(sqlite_select_query)
        sqlite_connection.commit()
        nb_row = cursor.rowcount
        logging.info(
            f"added {nb_row} row",
        )
        cursor.close()

    except sqlite3.Error as error:
        logging.error("Error while adding message", error)
    finally:
        if sqlite_connection:
            sqlite_connection.close()

    return nb_row > 0


def select_message(nb, start, forum):
    rows = []
    try:
        sqlite_connection, cursor = init_connection()
        logging.info("Connected getting message...")

        sqlite_select_query = (
            f"SELECT * FROM message WHERE id > {start} and forum = {forum} ORDER BY time LIMIT {nb};"
        )
        # sqlite_select_Query = f"SELECT name FROM sqlite_master WHERE type='table'"
        cursor.execute(sqlite_select_query)
        rows = cursor.fetchall()
        logging.info(f"selected row {len(rows)}")
        cursor.close()

    except sqlite3.Error as error:
        logging.info("Error while getting message", error)
    finally:
        if sqlite_connection:
            sqlite_connection.close()

    return rows

def init_connection():
    sqlite_connection = sqlite3.connect(DB_NAME)
    cursor = sqlite_connection.cursor()
    return sqlite_connection, cursor


if __name__ == "__main__":
    init_db()
    print(select_message())
    print(insert_message("bob", "", "hi there", 1))
    print(select_message(forum=0))
