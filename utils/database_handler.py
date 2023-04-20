from typing import Optional
import sqlite3
from models.base_entity import BaseEntity
from utils.loggerX import Logger

logger = Logger(__name__)

class DatabaseHandler:
    """Handles database operations for meals."""

    def __init__(self, db_name: str = "data/test_db_handler_2.db"):
        self.db_name = db_name
        self.db_conn = None
        self._initialize_database()

    def _initialize_database(self):
        logger.debug("Initializing database...")
        with sqlite3.connect(self.db_name) as conn:
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
            self.db_conn = conn
            logger.debug("meals, days, weeks tables initialized.")

    def save(self, entity: BaseEntity) -> BaseEntity:
        '''Save an entity to the database.'''
        with self.db_conn as conn:
            cursor = conn.cursor()
            keys, values, placeholders = self.get_entity_keys_values_placeholders(entity)
            query = f"INSERT INTO {entity.table_name} ({keys}) VALUES ({placeholders})"
            logger.debug(query)
            cursor.execute(query, tuple(values))
            conn.commit()
            entity.id = cursor.lastrowid
            logger.debug(f"Entity saved successfully to {entity.table_name}.")
            logger.log_class_properties(entity)
            return entity

    def update(self, entity: BaseEntity) -> BaseEntity:
        '''Update an entity in the database.'''
        with self.db_conn as conn:
            cursor = conn.cursor()
            set_clause = ', '.join([f"{key} = ?" for key in entity.to_dict().keys() if key != 'id'])
            query = f"UPDATE {entity.table_name} SET {set_clause} WHERE id = ?"
            values = tuple(v for k, v in entity.to_dict().items() if k != 'id') + (entity.id,)
            cursor.execute(query, values)
            conn.commit()
            logger.debug(f"Entity updated successfully in {entity.table_name}.")
            logger.log_class_properties(entity)
            return entity

    def delete(self, entity: BaseEntity) -> bool:
        '''Delete an entity from the database.'''
        conn = self.db_conn
        cursor = conn.cursor()
        query = f"DELETE FROM {entity.table_name} WHERE id = ?"
        logger.debug(query)
        cursor.execute(query, (entity.id,))
        conn.commit()
        if cursor.rowcount > 0:
            logger.debug(f"Entity deleted successfully from {entity.table_name}.")
            logger.log_class_properties(entity)
            return True
        return cursor.rowcount > 0

    def read(self, entity_class: type, entity_id: int) -> Optional[BaseEntity]:
        '''Read an entity from the database.'''
        with self.db_conn as conn:
            cursor = conn.cursor()
            query = f"SELECT * FROM {entity_class.table_name} WHERE id = ?"
            logger.debug(query)
            cursor.execute(query, (entity_id,))
            row = cursor.fetchone()
            if row:
                row_dict = self.create_row_dict(cursor, row)
                entity = entity_class.from_database(database_handler=self, row_dict=row_dict)
                logger.debug(f"Entity read successfully from {entity_class.table_name}.")
                return entity
            else:
                logger.debug(f"Entity with id {entity_id} not found in {entity_class.table_name}.")
                return None

    def get_entity_keys_values_placeholders(self, entity: BaseEntity):
        '''Get the keys, values and placeholders for an entity.'''
        entity_dict = entity.to_dict()
        keys = ', '.join(entity_dict.keys())
        values = tuple(entity_dict.values())
        placeholders = ', '.join(['?'] * len(entity_dict))
        return keys, values, placeholders

    def create_row_dict(self, cursor, row):
        '''Create a dictionary from a row.'''
        row_dict = {}
        for idx, col in enumerate(cursor.description):
            row_dict[col[0]] = row[idx]
        return row_dict
