import unittest
from utils.database_handler import DatabaseHandler
from models.meal import Meal
from models.day import Day
from models.week import Week

class TestDatabaseHandler(unittest.TestCase):
    '''Test the DatabaseHandler class.'''

    def setUp(self):
        self.db_handler = DatabaseHandler("data/test_database_handler.db")
        self.meal = Meal('Meat and Stuff',
                         ["Meat", "Onions", "Peppers"],
                         ["Cut Meat", "etc, etc..."],
                         30,
                         db_handler=self.db_handler)
        self.day = Day('Monday', db_handler=self.db_handler)
        self.week = Week(db_handler=self.db_handler)
        self.create_test_table()

    def tearDown(self):
        self.drop_test_tables()

    def create_test_table(self):
        '''Create a test table for testing the database handler.'''
        conn = self.db_handler.db_conn
        cursor = conn.cursor()
        cursor.execute("""
        CREATE TABLE IF NOT EXISTS meals (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            ingredients TEXT NOT NULL,
            prep_steps TEXT NOT NULL,
            cook_time INTEGER NOT NULL,
            protein TEXT NOT NULL,
            day_id TEXT
        )
        """)
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
        cursor.execute("""
        CREATE TABLE IF NOT EXISTS weeks (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            start_date TEXT,
            sun INTEGER,
            mon INTEGER,
            tue INTEGER,
            wed INTEGER,
            thu INTEGER,
            fri INTEGER,
            sat INTEGER
        )
        """)
        conn.commit()

    def drop_test_tables(self):
        '''Drop the test table.'''
        conn = self.db_handler.db_conn
        cursor = conn.cursor()
        cursor.execute("DROP TABLE IF EXISTS test_table")
        conn.commit()

    def test_initialize_database(self):
        '''Test that the database is initialized correctly.'''
        self.assertIsNotNone(self.db_handler.db_conn)

    def test_save_success(self):
        '''Test that an entity can be saved to the database.'''
        test_entity = self.day
        saved_entity = self.db_handler.save(test_entity)
        self.assertIsNotNone(saved_entity.id)

    def test_update_success(self):
        '''Test that an entity can be updated in the database.'''
        test_entity = self.meal
        saved_entity = self.db_handler.save(test_entity)
        saved_entity.name = 'Even More Meat'
        updated_entity = self.db_handler.update(saved_entity)
        self.assertEqual(updated_entity.name, 'Even More Meat')

    def test_delete_success(self):
        '''Test that an entity can be deleted from the database.'''
        test_entity = self.week
        saved_entity = self.db_handler.save(test_entity)
        self.assertTrue(self.db_handler.delete(saved_entity))

    def test_read_success(self):
        '''Test that an entity can be read from the database.'''
        test_entity = Day('Monday', db_handler=self.db_handler)
        saved_entity = self.db_handler.save(test_entity)
        read_entity = self.db_handler.read(Day, saved_entity.id)
        self.assertIsNotNone(read_entity)
        self.assertEqual(saved_entity.id, read_entity.id)

    def test_read_fail(self):
        '''Test that an entity cannot be read from the database.'''
        self.assertIsNone(self.db_handler.read(Day, -1))

if __name__ == '__main__':
    unittest.main()
