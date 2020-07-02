import unittest
import sqlite3
import sql_statements as sql

class TestSQLStatements(unittest.TestCase):
    def setUp(self):
        self.base_tables = {
            0: ['workout',
                ['workout_id', 'date'],
                sql.create_workout_t],
            1: ['cardio',
                ['cardio_id', 'name', 'time', 'dist', 'cals'],
                sql.create_cardio_t],
            2: ['exercise',
                ['exercise_id', 'name', 'body_part', 'reps', 'sets', 'time'],
                sql.create_exercises_t]
        }
        self.join_tables = {
            0: [['workoutCardio', 'workout', 'cardio'],
                ['workout_id', 'cardio_id'],
                sql.create_workoutCardio_t],
            1: [['workoutExercise', 'workout', 'exercise'],
                ['workout_id', 'cardio_id'],
                sql.create_workoutExercise_t]
        }
        self.conn = sqlite3.connect(":memory:")
        self.cursor = self.conn.cursor()
        self.master_table = """SELECT name FROM sqlite_master WHERE type="table";"""

    def test_base_tables(self):
        for key in self.base_tables:
            self.create_base_tables(key)

    def create_base_tables(self, num):
        #set up test table
        self.cursor.execute(self.base_tables[num][2])
        self.conn.commit()
        #get table names
        self.cursor.execute(self.master_table)
        tables = self.cursor.fetchall()
        #test table names
        self.assertEqual(len(tables), 1)
        self.assertEqual(self.base_tables[num][0], tables[0][0])
        #get fields of table
        self.cursor.execute("SELECT * FROM " + self.base_tables[num][0])
        fields = [description[0] for description in self.cursor.description]
        #test fields
        self.assertEqual(self.base_tables[num][1], fields)
        self.cursor.execute(f"DROP TABLE IF EXISTS " + self.base_tables[num][0])

    def test_create_woc_join_tables(self):
        #setup 2 base tables and join table
        self.cursor.execute(self.base_tables[0][2])
        self.conn.commit()
        self.cursor.execute(self.base_tables[1][2])
        self.conn.commit()
        self.cursor.execute(self.join_tables[0][2])
        self.conn.commit()

        self.cursor.execute(self.master_table)
        tables = [table[0] for table in self.cursor.fetchall()]

        self.assertEqual(sorted(self.join_tables[0][0]), sorted(tables))

    def test_create_woe_join_tables(self):
        #setup 2 base tables and join table
        self.cursor.execute(self.base_tables[0][2])
        self.conn.commit()
        self.cursor.execute(self.base_tables[2][2])
        self.conn.commit()
        self.cursor.execute(self.join_tables[1][2])
        self.conn.commit()

        self.cursor.execute(self.master_table)
        tables = [table[0] for table in self.cursor.fetchall()]

        self.assertEqual(sorted(self.join_tables[1][0]), sorted(tables))

    def tearDown(self):
        self.cursor.close()
        self.conn.close()

if __name__ == "__main__":
    SUITE = unittest.TestLoader().loadTestsFromTestCase(TestSQLStatements)
    unittest.TextTestRunner(verbosity=2).run(SUITE)
