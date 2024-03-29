from models.base_entity import BaseEntity
from utils.loggerX import Logger

logger = Logger(__name__)

class Meal(BaseEntity):
    """Meal class for storing meal data."""
    table_name = "meals"
    def __init__(self, name, ingredients, prep_steps, cook_time, day_id=-1, db_handler=None):
        super().__init__(db_handler)
        self.name = name
        self.ingredients = ingredients
        self.prep_steps = prep_steps
        self.cook_time = cook_time
        self.protein = self.identify_protein()
        self.day_id = day_id
        self.day_object = None

    @classmethod
    def from_database(cls, database_handler, row_dict):
        '''Create a new object from a database row.'''
        name = row_dict['name']
        ingredients = row_dict['ingredients']
        prep_steps = row_dict['prep_steps']
        cook_time = row_dict['cook_time']
        day_id = row_dict['day_id']
        meal = cls(name, ingredients, prep_steps, cook_time, day_id, database_handler)
        meal.protein = row_dict['protein']
        meal.id = row_dict['id']
        return meal

    def identify_protein(self):
        '''Identify the protein in the meal. Used to schedule defrosting.'''
        proteins = ("beef", "chicken", "pork", "fish", "tofu", "eggs", "cheese", "meat")
        for ingredient in self.ingredients:
            for word in ingredient.split():
                if word.lower() in proteins:
                    return word

    def set_day_object(self, day_object):
        '''Set the day object.'''
        self.day_object = day_object

    def to_dict(self) -> dict:
        '''
        Convert the object's properties to a dictionary.
        Do not provide the ID, it is auto-generated by the database.
        '''
        return {
                'name': self.name,
                'ingredients': ";".join(self.ingredients),
                'prep_steps': ";".join(self.prep_steps),
                'cook_time': self.cook_time,
                'protein': self.protein,
                'day_id': self.day_id
                }

    def __str__(self):
        return f"{self.name} ({self.cook_time} minutes) - Protein: {self.protein}"
