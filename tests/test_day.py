import unittest
from datetime import date
from utils.database_handler import DatabaseHandler
from models.day import Day
from utils.constants import *

class TestDay(unittest.TestCase):
    '''Test the Day class.'''

    def setUp(self):
        self.db_handler = DatabaseHandler(TEST_DAY_DB_FILE)
        self.create_test_table()
        self.test_day = Day("Monday", self.db_handler)

    def tearDown(self):
        self.drop_test_tables()

    def create_test_table(self):
        '''Create a test table for testing the database handler.'''
        with self.db_handler.db_conn as conn:
            cursor = conn.cursor()
            cursor.execute("""
            CREATE TABLE IF NOT EXISTS days (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                week_id INTEGER,
                name TEXT NOT NULL,
                meals TEXT,
                date TEXT
            )
            """)
            conn.commit()

    def drop_test_tables(self):
        '''Drop the test table.'''
        with self.db_handler.db_conn as conn:
            cursor = conn.cursor()
            cursor.execute("DROP TABLE IF EXISTS days")
            conn.commit()

    def test_to_dict(self):
        '''Test that a day can be converted to a dictionary.'''
        self.test_day.week_id = 1
        self.test_day.date = "2023-04-24"
        expected_dict = {
            'week_id': 1,
            'name': 'Monday',
            'meals': '',
            'date': "2023-04-24"
        }
        self.assertEqual(self.test_day.to_dict(), expected_dict)

    def test_from_database(self):
        '''Test that a day can be created from a database row.'''
        self.test_day.save()
        day_from_db = Day.from_database(self.db_handler, {'id': self.test_day.id, 'name': 'Monday'})
        self.assertEqual(self.test_day.id, day_from_db.id)
        self.assertEqual(self.test_day.name, day_from_db.name)

    def test_set_day_date(self):
        '''Test that the day date is set correctly.'''
        start_date = date(2023, 4, 23)
        self.test_day.set_day_date(start_date)
        self.assertEqual(self.test_day.date, date(2023, 4, 24))

if __name__ == '__main__':
    unittest.main()
