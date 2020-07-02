"""
This module contains the class code for the database handling. Class will
initialize and check to see if the database exists upon DBHandler object
creation. If there already is a created database, the object will initialize
a connection to the database. Otherwise, the object will create the database
in the default location within the program directory.

Class is also used to add/delete rows to tables.

All SQL code is found within sql_statements.py.

EXAMPLE: DB = DBHandler() - initializes new DBHandler class and does the check
                            if the database exists.
         DB.insert_workout(date) - inserts a workout into the workout table
                                   when given a date as a string.
         DB.insert_exercise(exercise) - inserts an exercise when given a valid
                                        exercise tuple.

#TODO: update when changed from print statements
Program will currently throw errors and halt the program where it hit the error.
Currently only displayed as console statements.
"""

import sqlite3
from sqlite3 import Error
from os.path import isfile

import sql_statements
from sql_statements import create_table_codes

class DBHandler:
    """

    """
    def __init__(self):
        #default location for db
        self.location = r"database\workouts.db"
        self.conn = None
        if not isfile(self.location):
            self._initialize_db()
        else:
            self._create_connection()

    def _create_connection(self):
        """
        creates a database connection to a sqlite3 database using location.
        returns connection or error if fails
        """
        try:
            self.conn = sqlite3.connect(self.location)
        except Error:
            return Error
        return None

    def _initialize_db(self):
        """
        Sets up database if it doesn't already exist. Starts with creating database
        then adds the tables to it. Upon error, stops program.
        """
        #connect to database, throws error and returns upon failure
        error = self._create_connection()
        if error:
            #TODO: once GUI is made, make more elaborate error handling
            print("Database setup error:", error)
            return

        #attempt to create the sql tables as found in sql_codes.py
        for create_table_code in create_table_codes:
            error = self._create_table(create_table_code)
            if error:
                #TODO: once GUI is made, make more elaborate error handling
                print("Table creation error:", error)
                return

    def _create_table(self, code):
        """
        creates a table in a database through connection conn.
        returns None upon success, returns error upon error

        :param code: table creation sql code
        """
        try:
            cursor = self.conn.cursor()
            cursor.execute(code)
            cursor.close()
            return None
        except Error:
            cursor.close()
            return Error

    #TODO: validation checking on date
    def insert_workout(self, date):
        """
        Inserts row into workout table
        :param date: date in string format
        """
        cursor = self.conn.cursor()
        cursor.execute(sql_statements.insert_workout, date)
        cursor.close()

    #TODO: validation checking on exercise
    def insert_exercise(self, exercise):
        """
        Inserts row into workout table
        :param exercise: exercise in tuple form (name, body_part, reps, sets, time)
                        as (text, text, int, int, real)
        """
        cursor = self.conn.cursor()
        cursor.execute(sql_statements.insert_exercise, exercise)
        cursor.close()
