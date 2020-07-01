import sqlite3
from sql_codes import create_table_codes
from sqlite3 import Error

def initialize():
    location = r"database\workouts.db"

    #connect to database, throws error and returns upon failure
    result = create_connection(location)
    if result[0] == 0:
        print("Database setup error:", result[1])
        return
    else:
        conn = result[1]

    #attempt to create the sql tables as found in sql_codes.py
    for create_table_code in create_table_codes:
        print("H")
        error = create_table(conn, create_table_code)
        if error:
            print("Table creation error:", error)
            return


def create_connection(location):
    """
    creates a database connection to a sqlite3 database using location.
    returns connection or error if fails

    :param location: string that represents the directory location and
        database name

    """
    conn = None
    try:
        conn = sqlite3.connect(location)
    except Error as e:
        return (0, e)
    finally:
        if conn:
            return (1, conn)

def create_table(conn, code):
    """
    creates a table in a database through connection conn.
    returns None upon success, returns error upon error

    :param conn: connection to the workout database
    :param code: table creation sql code
    """
    try:
        cursor = conn.cursor()
        cursor.execute(code)
        cursor.close()
        return None
    except Error as e:
        cursor.close()
        return e

if __name__ == "__main__":
    initialize()