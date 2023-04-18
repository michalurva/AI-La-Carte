import os
from datetime import date
from utils.database_handler import DatabaseHandler
from utils.calendar_csv_handler import CalendarCSVHandler
from utils.meal_csv_handler import MealCSVHandler
from utils.loggerX import Logger
from tests.test_models import main as test_models
from models.week import Week

logger = Logger(__name__)
FILE_NAME_MEALS_CSV = "data/unassigned_meals.csv"
FILE_NAME_MEALS_COPY = "data/unassigned_meals_copy.csv"
FILE_NAME_CALENDAR_CSV = "data/calendar.csv"
DB_FILE_NAME = "data/meal_planner.db"

#initialize the database
db_handler = DatabaseHandler(DB_FILE_NAME)

def main():
    """A quick test of all classes"""
    unassigned_meals = []
    meal_csv_handler = MealCSVHandler()
    calendar_csv_handler = CalendarCSVHandler()
    week = Week(date.today())
    #save the week to the database
    week_id = db_handler.create_week(week)
    logger.debug(f"week id: {week_id} saved to database")

    #load the week from the database
    loaded_week = db_handler.read_week(week_id)
    logger.debug(f"week id: {loaded_week.id} loaded from database")
    
    #load the meals from the csv file
    meals = meal_csv_handler.load_from_csv(FILE_NAME_MEALS_CSV)

    #save the meals to the database
    for meal in meals:
        unassigned_meals.append(db_handler.create_meal(meal))
        logger.debug(f"meal: {meal.name} id: {meal.id} saved to database")

    #load the meals from the database
    loaded_meals = []
    for meal in unassigned_meals:
        meal = db_handler.read_meal(meal.id)
        loaded_meals.append(meal)
        logger.debug(f"meal: {meal.name} id: {meal.id} loaded from database")


    #assign the meals to each day the week
    loaded_week.mon.add_meal(loaded_meals[0])
    loaded_week.tue.add_meal(loaded_meals[1])
    loaded_week.wed.add_meal(loaded_meals[2])
    loaded_week.thu.add_meal(loaded_meals[3])
    loaded_week.fri.add_meal(loaded_meals[4])

    #save the meals in calendar format
    calendar_csv_handler.save_to_csv(loaded_week, "data/calendar.csv")
    #clean up the database
    clean_up()

def reload_xml(meal_csv_handler):
    '''Reload the meals from the database to the csv file'''
    #load the meals from the database
    meals = db_handler.read_all_meals()
    #save the meals to a new csv file
    meal_csv_handler.save_to_csv(meals, FILE_NAME_MEALS_COPY)
    for meal in meals:
        logger.log_class_properties(meal)
        db_handler.delete_meal(meal)

def clean_up():
    """Clean up the database and test files"""
    if os.path.isfile(FILE_NAME_MEALS_COPY):
        os.remove(FILE_NAME_MEALS_COPY)
    db_handler.drop_tables()

if __name__ == "__main__":
    main()
    clean_up()
    test_models()
