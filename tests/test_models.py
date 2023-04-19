import unittest

from tests.test_database import TestDatabaseHandler
from tests.test_meal_csv_handler import TestMealCSVHandler
from tests.test_calendar_csv_handler import TestCalendarCSVHandler
from tests.test_base_entity import TestBaseEntity
from tests.test_day import TestDay
from tests.test_meal import TestMeal
from tests.test_week import TestWeek

def suite():
    """Test suite for all tests in the tests folder."""
    test_suite = unittest.TestSuite()

    #load model test cases
    database_test = unittest.TestLoader().loadTestsFromTestCase(TestDatabaseHandler)
    test_meal_csv_handler = unittest.TestLoader().loadTestsFromTestCase(TestMealCSVHandler)
    test_calendar_csv_handler = unittest.TestLoader().loadTestsFromTestCase(TestCalendarCSVHandler)
    test_base_entity = unittest.TestLoader().loadTestsFromTestCase(TestBaseEntity)
    test_day = unittest.TestLoader().loadTestsFromTestCase(TestDay)
    test_meal = unittest.TestLoader().loadTestsFromTestCase(TestMeal)
    test_week = unittest.TestLoader().loadTestsFromTestCase(TestWeek)

    #add test cases to test suite
    test_suite.addTest(database_test)
    test_suite.addTest(test_meal_csv_handler)
    test_suite.addTest(test_calendar_csv_handler)
    test_suite.addTest(test_base_entity)
    test_suite.addTest(test_day)
    test_suite.addTest(test_meal)
    test_suite.addTest(test_week)

    return test_suite

def main():
    """Run the test suite."""
    runner = unittest.TextTestRunner()
    runner.run(suite())

if __name__ == '__main__':
    main()
