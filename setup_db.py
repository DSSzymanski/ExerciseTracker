"""
This module contains the code for setting up a database if it doens't already
exist. Only call to module is to initialize, which will call the functions for
creating the database and creating the tables.

EXAMPLE: setup_db.initialize()

#TODO: update when changed from print statements
Program will currently throw errors and halt the program where it hit the error.
Currently only displayed as console statements.
"""

import sqlite3
from sqlite3 import Error
from sql_codes import create_table_codes

def initialize():
    """
    Sets up database if it doesn't already exist. Starts with creating database
    then adds the tables to it. Upon error, stops program.
    """
    #default location
    location = r"database\workouts.db"

    #connect to database, throws error and returns upon failure
    result = _create_connection(location)
    if result[0] == 0:
        #TODO: once GUI is made, make more elaborate error handling
        print("Database setup error:", result[1])
        return
    conn = result[1]

    #attempt to create the sql tables as found in sql_codes.py
    for create_table_code in create_table_codes:
        error = _create_table(conn, create_table_code)
        if error:
            #TODO: once GUI is made, make more elaborate error handling
            print("Table creation error:", error)
            return

#TODO: move somewhere else? boiler plate code that won't just be used here
def _create_connection(location):
    """
    creates a database connection to a sqlite3 database using location.
    returns connection or error if fails

    :param location: string that represents the directory location and
        database name

    """
    conn = None
    try:
        conn = sqlite3.connect(location)
    except Error:
        return (0, Error)
    finally:
        if conn:
            return (1, conn)

def _create_table(conn, code):
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
    except Error:
        cursor.close()
        return Error
