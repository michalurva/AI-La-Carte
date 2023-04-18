from models.meal import Meal
from models.day import Day
from models.week import Week
from utils.database_handler2 import DatabaseHandler
from utils.loggerX import Logger

logger = Logger(__name__)

def main():
    '''test method'''
    db_handle = DatabaseHandler()
    test_meal(db_handle)
    test_day(db_handle)
    test_week(db_handle)

def test_meal(db_handler):
    '''Main method for testing the Meal class.'''
    meal = Meal('Meat and Stuff', ["Meat", "Onions", "Peppers"], ["Cut Meat", "etc, etc..."], 30, db_handler=db_handler)
    meal = db_handler.save(meal)
    logger.log_class_properties(meal)
    meal = db_handler.read(Meal, meal.id)
    logger.log_class_properties(meal)
    meal.name = 'Meat and Good Stuff'
    meal = db_handler.update(meal)
    logger.log_class_properties(meal)
    is_deleted = db_handler.delete(meal)
    logger.debug(f"day deleted: {is_deleted}")

def test_day(db_handler):
    '''Main method for testing the Day class.'''
    day = Day('Monday', db_handler=db_handler)
    day = db_handler.save(day)
    logger.log_class_properties(day)
    day = db_handler.read(Day, day.id)
    logger.log_class_properties(day)
    day.name = 'Tuesday'
    day = db_handler.update(day)
    logger.log_class_properties(day)
    is_deleted = db_handler.delete(day)
    logger.debug(f"day deleted: {is_deleted}")

def test_week(db_handler):
    '''Main method for testing the Day class.'''
    week = Week(db_handler=db_handler)
    week = db_handler.save(week)
    logger.log_class_properties(week)
    week = db_handler.read(Week, week.id)
    logger.log_class_properties(week)
    week.mon = 'Tuesweek'
    week = db_handler.update(week)
    logger.log_class_properties(week)
    is_deleted = db_handler.delete(week)
    logger.debug(f"week deleted: {is_deleted}")

if __name__ == '__main__':
    main()
