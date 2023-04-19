import unittest
from models.meal import Meal
from utils.database_handler import DatabaseHandler

class TestMeal(unittest.TestCase):
    '''Test the Meal class.'''
    def setUp(self):
        self.db_handler = DatabaseHandler()
        self.meal = Meal("Spaghetti Bolognese",
                         ["pasta", "beef", "tomato sauce"],
                         ["Cook pasta", "Prepare sauce"],
                         30,
                         db_handler=self.db_handler)

    def tearDown(self):
        self.db_handler.delete(self.meal)
        self.db_handler.db_conn.close()

    def test_init(self):
        '''Test that the meal is initialised correctly.'''
        self.assertIsNotNone(self.meal)
        self.assertEqual(self.meal.name, "Spaghetti Bolognese")

    def test_from_database(self):
        '''Test that the meal is initialised correctly from the database.'''
        meal_data = {
            'name': 'Spaghetti Bolognese',
            'ingredients': 'pasta;beef;tomato sauce',
            'prep_steps': 'Cook pasta;Prepare sauce',
            'cook_time': 30,
            'protein': 'beef',
            'day_id': -1
        }
        self.db_handler.save(self.meal)
        retrieved_meal = self.db_handler.read(Meal, self.meal.id)

        self.assertEqual(retrieved_meal.name, meal_data["name"])
        self.assertEqual(retrieved_meal.ingredients, meal_data["ingredients"])
        self.assertEqual(retrieved_meal.prep_steps, meal_data["prep_steps"])
        self.assertEqual(retrieved_meal.cook_time, meal_data["cook_time"])
        self.assertEqual(retrieved_meal.protein, meal_data["protein"])

    def test_identify_protein(self):
        '''Test that the meal identifies the meal's protein correctly.'''
        self.assertEqual(self.meal.identify_protein(), "beef")

    def test_to_dict(self):
        '''Test that the meal is converted to a dictionary correctly.'''
        meal_data = {
            'name': 'Spaghetti Bolognese',
            'ingredients': 'pasta;beef;tomato sauce',
            'prep_steps': 'Cook pasta;Prepare sauce',
            'cook_time': 30,
            'protein': 'beef',
            'day_id': -1
        }
        self.assertEqual(self.meal.to_dict(), meal_data)

    def test_str(self):
        '''Test that the meal is converted to a string correctly.'''
        self.assertEqual(str(self.meal), "Spaghetti Bolognese (30 minutes) - Protein: beef")

if __name__ == "__main__":
    unittest.main()
