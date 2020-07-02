#sql code to create workout table
create_workout_t = """ CREATE TABLE IF NOT EXISTS workout (
                            workout_id integer PRIMARY KEY,
                            date text
                        );"""

#sql code to create exercise table
create_exercises_t = """CREATE TABLE IF NOT EXISTS exercise (
                            exercise_id integer PRIMARY KEY,
                            name text,
                            body_part text,
                            reps integer,
                            sets integer,
                            time real
                        );"""

#sql code to create cardio table
create_cardio_t = """CREATE TABLE IF NOT EXISTS cardio (
                        cardio_id integer PRIMARY KEY,
                        name text,
                        time real,
                        dist real,
                        cals integer
                    );"""

#sql code to create a table to link workouts and cardio table entries
create_workout_cardio_t = """CREATE TABLE IF NOT EXISTS workoutCardio (
                                    workout_id integer,
                                    cardio_id integer,
                                    PRIMARY KEY(workout_id, cardio_id),
                                    FOREIGN KEY(workout_id) REFERENCES workout(workout_id),
                                    FOREIGN KEY(cardio_id) REFERENCES cardio(cardio_id)
                                );"""

#sql code to create a table to link workouts and exercise table entries
create_workout_exercise_t = """CREATE TABLE IF NOT EXISTS workoutExercise (
                                    workout_id integer,
                                    exercise_id integer,
                                    PRIMARY KEY(workout_id, exercise_id),
                                    FOREIGN KEY(workout_id) REFERENCES workout(workout_id),
                                    FOREIGN KEY(exercise_id) REFERENCES exercise(exercise_id)
                                );"""

#list of all table creation sql codes
create_table_codes = [
        create_workout_t,
        create_exercises_t,
        create_cardio_t,
        create_workout_cardio_t,
        create_workout_exercise_t
        ]

#insert row into workout table
insert_workout = """INSERT INTO workout(date) VALUES (?)"""

#insert row into exercise table REMEMBER TO CONVERT TIME TO REAL
insert_exercise = """INSERT INTO exercise(name, body_part, reps, sets, time)
                    VALUES(?, ?, ?, ?, ?)"""

#insert row into cardio table REMEMBER TO CONVERT TIME, DIST TO REALS
insert_cardio = """INSERT INTO cardio (name, time, dist, cals)
                    VALUES(?, ?, ?, ?)"""

insert_workoutCardio = """"""