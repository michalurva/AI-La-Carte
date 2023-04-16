import unittest
import sqlite3
from utils.database_handler import DatabaseHandler
from models.day import Day
from models.week import Week
from models.meal import Meal

TEST_DB_NAME = "data/meal_planner_test.db"

class TestDatabaseHandler(unittest.TestCase):
    '''Test the methods in database handler.'''
    def setUp(self):
        self._drop_tables()

        self.week = Week()
        #initialize a meal per day
        self.meal1 = Meal("Beef and Broccoli Stir-Fry",
                         ["beef", "broccoli", "onion", "garlic", "soy sauce", "oyster sauce", "honey", "jasmine rice"],
                         ["Thinly slice beef, chop broccoli, mince onion and garlic"],
                         30,
                         "Monday")
        self.meal2 = Meal("Chicken Piccata",
                         ["chicken breast", "flour", "salt", "pepper",
                          "lemon juice", "capers", "white wine", "garlic", "onion", "brassicas"],
                         ["Pound chicken breasts thin, dredge in flour, season with salt and pepper, sauté garlic and onion"],
                         40,
                         "Tuesday")
        self.meal3 = Meal("Pork Tenderloin with Balsamic Glaze",
                         ["pork tenderloin", "balsamic vinegar", "honey", "garlic", "rosemary", "carrots", "bell peppers", "onions", "farro"],
                         ["Prepare glaze with balsamic vinegar, honey, garlic, and rosemary, roast vegetables"],
                         45,
                         "Wednesday")
        self.meal4 = Meal("Vegetarian Stuffed Peppers",
                         ["bell peppers", "short-grain rice", "vegetable broth", "onion", "garlic", "tomato sauce", "mushrooms", "spinach", "black beans", "cheese"],
                         ["Halve and deseed bell peppers, cook rice, sauté mushrooms, spinach, and black beans, stuff peppers and top with cheese"],
                         50,
                         "Thursday")
        self.meal5 = Meal("One-Pan Lemon Herb Chicken and Rice",
                         ["chicken thighs", "garlic", "onion", "rosemary", "thyme", "parsley", "short-grain rice", "jasmine rice", "chicken broth", "lemon juice", "lemon zest"],
                         ["Cook chicken thighs with garlic, onion, and herbs, add rice and chicken broth, season with lemon juice and zest"],
                         60,
                         "Friday")

        #add meals to days
        self.week.days[1].add_meal(self.meal1)
        self.week.days[2].add_meal(self.meal2)
        self.week.days[3].add_meal(self.meal3)
        self.week.days[4].add_meal(self.meal4)
        self.week.days[5].add_meal(self.meal5)

    def tearDown(self) -> None:
        self._drop_tables()

    def test_create_day(self):
        '''#create day should return the row id of the last row inserted into the database.'''
        db_handler = DatabaseHandler(TEST_DB_NAME)
        last_row_id = db_handler.create_day(self.week.days[1])
        self.assertEqual(last_row_id, 1)

    def test_read_day(self):
        '''read day should return a day object.'''
        db_handler = DatabaseHandler(TEST_DB_NAME)
        db_handler.create_day(self.week.days[1])
        day = db_handler.read_day(1)
        self.assertIsInstance(day, Day)

    def test_create_week(self):
        '''create week should return the row id of the last row inserted into the database.'''
        db_handler = DatabaseHandler(TEST_DB_NAME)
        last_row_id = db_handler.create_week(self.week)
        self.assertEqual(last_row_id, 1)

    def test_read_week(self):
        '''read week should return a week object.'''
        db_handler = DatabaseHandler(TEST_DB_NAME)
        db_handler.create_week(self.week)
        week = db_handler.read_week(1)
        self.assertIsInstance(week, Week)

    def test_create_meal(self):
        '''create meal should return the row id of the last row inserted into the database.'''
        db_handler = DatabaseHandler(TEST_DB_NAME)
        last_row_id = db_handler.create_meal(self.meal1)
        self.assertEqual(last_row_id, 1)

    def test_read_meal(self):
        '''read meal should return a meal object.'''
        db_handler = DatabaseHandler(TEST_DB_NAME)
        db_handler.create_meal(self.meal1)
        meal = db_handler.read_meal(1)
        self.assertIsInstance(meal, Meal)
        self.assertEqual(meal.name, "Beef and Broccoli Stir-Fry")

    def test_read_all_meals(self):
        '''read all meals should return a list of meal objects.'''
        db_handler = DatabaseHandler(TEST_DB_NAME)
        db_handler.create_meal(self.meal1)
        db_handler.create_meal(self.meal2)
        db_handler.create_meal(self.meal3)
        db_handler.create_meal(self.meal4)
        db_handler.create_meal(self.meal5)
        meals = db_handler.read_all_meals()
        self.assertIsInstance(meals, list)
        self.assertEqual(len(meals), 5)

    def test_update_meal(self):
        '''update meal should return the row id of the updated row.'''
        db_handler = DatabaseHandler(TEST_DB_NAME)
        db_handler.create_meal(self.meal1)
        self.meal1.name = "Beef and Broccoli Stir-Fry with Jasmine Rice"
        update_success = db_handler.update_meal(self.meal1)
        self.assertEqual(update_success, True)

    def test_delete_meal(self):
        '''delete meal should return the row id of the deleted row.'''
        db_handler = DatabaseHandler(TEST_DB_NAME)
        db_handler.create_meal(self.meal1)
        delete_success = db_handler.delete_meal(self.meal1)
        self.assertEqual(delete_success, True)

    def test_delete_week(self):
        '''delete week should return the row id of the deleted row.'''
        db_handler = DatabaseHandler(TEST_DB_NAME)
        db_handler.create_week(self.week)
        delete_success = db_handler.delete_week(self.week)
        self.assertEqual(delete_success, True)

    def test_delete_day(self):
        '''delete day should return the row id of the deleted row.'''
        db_handler = DatabaseHandler(TEST_DB_NAME)
        db_handler.create_day(self.week.days[1])
        delete_success = db_handler.delete_day(self.week.days[1])
        self.assertEqual(delete_success, True)

    def _drop_tables(self):
        '''clean up the database'''
        conn = sqlite3.connect(TEST_DB_NAME)
        cursor = conn.cursor()
        cursor.execute("DROP TABLE IF EXISTS days")
        cursor.execute("DROP TABLE IF EXISTS meals")
        cursor.execute("DROP TABLE IF EXISTS weeks")
        conn.commit()
        conn.close()

if __name__ == '__main__':
    unittest.main()
