import unittest
from models.meal import Meal

class TestMeal(unittest.TestCase):
    '''Test the Meal class.'''
    def setUp(self):
        self.meal = Meal("Beef and Broccoli Stir-Fry",
                         ["beef", "broccoli", "onion",
                          "garlic", "soy sauce", "oyster sauce",
                          "honey", "jasmine rice"],
                         ["Thinly slice beef, chop broccoli, mince onion and garlic"],
                         30,
                         "Monday")

    def tearDown(self):
        del self.meal

    def test_name(self):
        '''Test the name property.'''
        self.assertEqual(self.meal.name, "Beef and Broccoli Stir-Fry")

    def test_ingredients(self):
        '''Test the ingredients property.'''
        self.assertEqual(self.meal.ingredients,
                         ["beef", "broccoli", "onion",
                          "garlic", "soy sauce", "oyster sauce",
                          "honey", "jasmine rice"])

    def test_prep_steps(self):
        '''Test the prep_steps property.'''
        self.assertEqual(self.meal.prep_steps, [
            "Thinly slice beef, chop broccoli, mince onion and garlic"])

    def test_cook_time(self):
        '''Test the cook_time property.'''
        self.assertEqual(self.meal.cook_time, 30)

    def test_protein(self):
        '''Test the protein property.'''
        self.assertEqual(self.meal.protein, "beef")

    def test_id_initialized(self):
        '''id should not have be a value other than -1 until it has a record in the database.'''
        self.assertEqual(self.meal.id, -1)

if __name__ == '__main__':
    unittest.main()
