import unittest
from utils.database_handler import DatabaseHandler
from models.base_entity import BaseEntity

class TestEntity(BaseEntity):
    '''Test entity for testing the base entity class.'''
    table_name = 'test_table'

    def __init__(self, db_handler, **kwargs):
        super().__init__(db_handler)
        self.field1 = kwargs.get('field1', '')
        self.field2 = kwargs.get('field2', '')

    def to_dict(self) -> dict:
        return {
            'field1': self.field1,
            'field2': self.field2
        }

    @classmethod
    def from_database(cls, database_handler, row_dict):
        return cls(database_handler, field1=row_dict['field1'], field2=row_dict['field2'])

class TestBaseEntity(unittest.TestCase):
    '''Test the base entity class.'''

    def setUp(self):
        self.db_handler = DatabaseHandler("data/test_base_entity.db")
        self.create_test_table()
        self.test_entity = TestEntity(self.db_handler, field1='Test 1', field2='Test 2')

    def tearDown(self):
        self.drop_test_tables()

    def create_test_table(self):
        '''Create the test table.'''
        with self.db_handler.db_conn as conn:
            cursor = conn.cursor()
            cursor.execute("""
            CREATE TABLE IF NOT EXISTS test_table (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                field1 TEXT NOT NULL,
                field2 TEXT NOT NULL
            )
            """)
            conn.commit()

    def drop_test_tables(self):
        '''Drop the test table.'''
        with self.db_handler.db_conn as conn:
            cursor = conn.cursor()
            cursor.execute("DROP TABLE IF EXISTS test_table")
            conn.commit()

    def test_save_success(self):
        '''Test that an entity can be saved to the database.'''
        saved_entity = self.test_entity.save()
        self.assertIsNotNone(saved_entity.id)

    def test_update_success(self):
        '''Test that an entity can be updated in the database.'''
        saved_entity = self.test_entity.save()
        saved_entity.field1 = 'Updated Test 1'
        updated_entity = saved_entity.update()
        self.assertEqual(updated_entity.field1, 'Updated Test 1')

    def test_delete_success(self):
        '''Test that an entity can be deleted from the database.'''
        saved_entity = self.test_entity.save()
        self.assertTrue(saved_entity.delete())

if __name__ == '__main__':
    unittest.main()
