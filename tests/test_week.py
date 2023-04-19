import unittest
from datetime import date
from models.week import Week
from utils.database_handler import DatabaseHandler

class TestWeek(unittest.TestCase):
    '''Test the Week class.'''
    def setUp(self):
        self.db_handler = DatabaseHandler()
        self.week = Week(db_handler=self.db_handler)

    def tearDown(self):
        self.drop_test_tables()
        self.db_handler.db_conn.close()

    def drop_test_tables(self):
        '''Drop the test table.'''
        conn = self.db_handler.db_conn
        cursor = conn.cursor()
        cursor.execute("DROP TABLE IF EXISTS days")
        conn.commit()

    def test_init(self):
        '''Test that the week object is initialized correctly.'''
        self.assertIsNotNone(self.week)
        self.assertEqual(self.week.start_date, date.today().isoformat())

    def test_from_database(self):
        '''Test that the week object is initialized correctly from the database.'''
        week_data = {
            'start_date': '2023-04-18',
            'sun': 'Sunny',
            'mon': 'Cloudy',
            'tue': 'Rainy',
            'wed': 'Snowy',
            'thu': 'Windy',
            'fri': 'Foggy',
            'sat': 'Clear',
        }
        self.week.start_date = week_data["start_date"]
        self.week.sun = week_data["sun"]
        self.week.mon = week_data["mon"]
        self.week.tue = week_data["tue"]
        self.week.wed = week_data["wed"]
        self.week.thu = week_data["thu"]
        self.week.fri = week_data["fri"]
        self.week.sat = week_data["sat"]

        self.db_handler.save(self.week)
        retrieved_week = self.db_handler.read(Week, self.week.id)

        self.assertEqual(retrieved_week.start_date, week_data["start_date"])
        self.assertEqual(retrieved_week.sun, week_data["sun"])
        self.assertEqual(retrieved_week.mon, week_data["mon"])
        self.assertEqual(retrieved_week.tue, week_data["tue"])
        self.assertEqual(retrieved_week.wed, week_data["wed"])
        self.assertEqual(retrieved_week.thu, week_data["thu"])
        self.assertEqual(retrieved_week.fri, week_data["fri"])
        self.assertEqual(retrieved_week.sat, week_data["sat"])

    def test_to_dict(self):
        '''Test that the week object is converted to a dictionary correctly.'''
        week_data = {
            'start_date': '2023-04-18',
            'sun': 'Sunny',
            'mon': 'Cloudy',
            'tue': 'Rainy',
            'wed': 'Snowy',
            'thu': 'Windy',
            'fri': 'Foggy',
            'sat': 'Clear',
        }
        self.week.start_date = week_data["start_date"]
        self.week.sun = week_data["sun"]
        self.week.mon = week_data["mon"]
        self.week.tue = week_data["tue"]
        self.week.wed = week_data["wed"]
        self.week.thu = week_data["thu"]
        self.week.fri = week_data["fri"]
        self.week.sat = week_data["sat"]

        self.assertEqual(self.week.to_dict(), week_data)

if __name__ == "__main__":
    unittest.main()
