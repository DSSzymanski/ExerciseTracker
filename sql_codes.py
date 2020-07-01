create_workout_t = """ CREATE TABLE IF NOT EXISTS workout (
                            workout_id integer PRIMARY KEY,
                            date text
                        );"""

create_exercises_t = """CREATE TABLE IF NOT EXISTS exercise (
                            exercise_id integer PRIMARY KEY,
                            name text,
                            body_part text,
                            reps integer,
                            sets integer,
                            time real
                        );"""

create_cardio_t = """CREATE TABLE IF NOT EXISTS cardio (
                        cardio_id integer PRIMARY KEY,
                        name text,
                        time real,
                        dist real,
                        cals integer
                    );"""

create_workout_cardio_t = """CREATE TABLE IF NOT EXISTS workoutCardio (
                                    workout_id integer,
                                    cardio_id integer,
                                    PRIMARY KEY(workout_id, cardio_id),
                                    FOREIGN KEY(workout_id) REFERENCES workout(workout_id),
                                    FOREIGN KEY(cardio_id) REFERENCES cardio(cardio_id)
                                );"""

create_workout_exercise_t = """CREATE TABLE IF NOT EXISTS workoutExercise (
                                    workout_id integer,
                                    exercise_id integer,
                                    PRIMARY KEY(workout_id, exercise_id),
                                    FOREIGN KEY(workout_id) REFERENCES workout(workout_id),
                                    FOREIGN KEY(exercise_id) REFERENCES exercise(exercise_id)
                                );"""
create_table_codes = [
        create_workout_t,
        create_exercises_t,
        create_cardio_t,
        create_workout_cardio_t,
        create_workout_exercise_t
        ]