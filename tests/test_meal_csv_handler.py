import unittest
import os
from models.meal import Meal
from utils.loggerX import Logger
from utils.meal_csv_handler import MealCSVHandler

logger = Logger("MealCSVHandlerTest")

class TestMealCSVHandler(unittest.TestCase):
    '''Test the MealCSVHandler class.'''
    def setUp(self):
        self.test_csv_file = "test_meals.csv"
        self.meals = [
            Meal("Beef and Broccoli Stir-Fry",
                 ["beef", "broccoli", "onion",
                  "garlic", "soy sauce", "oyster sauce",
                  "honey", "jasmine rice"],
                 ["Thinly slice beef", "chop broccoli", "mince onion and garlic"],
                 30,
                 "Monday"),
            # Add more test meals as needed
        ]

        with open(self.test_csv_file, 'w', newline='', encoding="UTF-8") as csvfile:
            csvfile.write("name,ingredients,prep_steps,cook_time,protein,day_of_week\n")
            for meal in self.meals:
                csvfile.write(f"{meal.name},{';'.join(meal.ingredients)},{';'.join(meal.prep_steps)},{meal.cook_time},{meal.protein},{meal.day_id}\n")
                logger.debug(f"{meal.name},{';'.join(meal.ingredients)},{';'.join(meal.prep_steps)},{meal.cook_time},{meal.protein},{meal.day_id}\n")

    def tearDown(self):
        os.remove(self.test_csv_file)

    def test_load_from_csv(self):
        '''Test the load_from_csv method.'''
        loaded_meals = MealCSVHandler.load_from_csv(self.test_csv_file)
        self.assertEqual(len(loaded_meals), len(self.meals))
        for meal, loaded_meal in zip(self.meals, loaded_meals):
            self.assertEqual(meal.name, loaded_meal.name)
            self.assertEqual(meal.ingredients, loaded_meal.ingredients)
            self.assertEqual(meal.prep_steps, loaded_meal.prep_steps)
            self.assertEqual(meal.cook_time, loaded_meal.cook_time)
            self.assertEqual(meal.protein, loaded_meal.protein)
            self.assertEqual(meal.day_id, loaded_meal.day_id)

    def test_save_to_csv(self):
        '''Test the save_to_csv method.'''
        saved_csv_file = "saved_meals.csv"
        MealCSVHandler.save_to_csv(self.meals, saved_csv_file)

        with open(saved_csv_file, 'r', encoding="UTF-8") as csvfile:
            lines = csvfile.readlines()

        self.assertEqual(len(lines), len(self.meals) + 1)  # header + meal lines

        os.remove(saved_csv_file)

if __name__ == '__main__':
    unittest.main()
