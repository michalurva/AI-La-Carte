from abc import ABC, abstractmethod

class BaseEntity(ABC):
    '''Base database entity class.'''

    table_name = ""

    def __init__(self, db_handler):
        # Initialize the object with a reference to the database handler
        self.db_handler = db_handler
        self.id = -1

    @abstractmethod
    def to_dict(self) -> dict:
        '''Convert the object's properties to a dictionary.'''

    @classmethod
    def from_database(cls, database_handler, row_dict):
        '''Create a new object from a database row.'''
        raise NotImplementedError("Subclasses must implement this method")

    def save(self):
        '''Save this object to the database.'''
        return self.db_handler.save(self)

    def update(self):
        '''Update this object in the database'''
        return self.db_handler.update(self)

    def delete(self):
        '''Delete this object from the database'''
        return self.db_handler.delete(self)
