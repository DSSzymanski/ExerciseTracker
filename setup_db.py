import sqlite3
import sql_codes
from sqlite3 import Error

def initialize():
    location = r"database\workouts.db"
    result = create_connection(location)
    if result[0] == 1:
        print("success")
    else:
        print("error", result[1])

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

if __name__ == "__main__":
    initialize()