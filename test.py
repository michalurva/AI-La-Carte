import os
from utils.database_handler import DatabaseHandler
from utils.meal_csv_handler import MealCSVHandler
from utils.loggerX import Logger
from tests.test_models import main as test_models

logger = Logger("test.log")
FILE_NAME = "data/meals.csv"
COPY_FILE_NAME = "data/meals_copy.csv"
DB_FILE_NAME = "data/meal_planner.db"

def main():
    """A quick test of all classes"""

    #initialize the database
    db_handler = DatabaseHandler()
    #initialize the csv handler
    csv_handler = MealCSVHandler()
    #load the meals from the csv file
    meals = csv_handler.load_from_csv(FILE_NAME)
    #save the meals to the database
    for meal in meals:
        db_handler.create_meal(meal)
    #load the meals from the database
    meals = db_handler.read_all_meals()
    #save the meals to a new csv file
    csv_handler.save_to_csv(meals, COPY_FILE_NAME)
    for meal in meals:
        logger.log_class_properties(meal)
        db_handler.delete_meal(meal)

def clean_up():
    """Clean up the database and test files"""
    if os.path.isfile(COPY_FILE_NAME):
        os.remove(COPY_FILE_NAME)

if __name__ == "__main__":
    # clean_up()
    # main()
    test_models()
