import unittest
from tests.test_database_handler import TestDatabaseHandler
from tests.test_meal import TestMeal
from tests.test_dates import TestDates
from tests.test_meal_csv_handler import TestMealCSVHandler
from tests.test_calendar_csv_handler import TestCalendarCSVHandler

def suite():
    """Test suite for all tests in the tests folder."""
    test_suite = unittest.TestSuite()

    #load model test cases
    meal_test = unittest.TestLoader().loadTestsFromTestCase(TestMeal)
    dates_test = unittest.TestLoader().loadTestsFromTestCase(TestDates)

    #load utility test cases
    meal_csv_handler_test = unittest.TestLoader().loadTestsFromTestCase(TestMealCSVHandler)
    calendar_csv_handler_test = unittest.TestLoader().loadTestsFromTestCase(TestCalendarCSVHandler)
    database_handler_test = unittest.TestLoader().loadTestsFromTestCase(TestDatabaseHandler)

    #add test cases to test suite
    test_suite.addTest(meal_test)
    test_suite.addTest(meal_csv_handler_test)
    test_suite.addTest(dates_test)
    test_suite.addTest(calendar_csv_handler_test)
    test_suite.addTest(database_handler_test)

    return test_suite

def main():
    """Run the test suite."""
    runner = unittest.TextTestRunner()
    runner.run(suite())

if __name__ == '__main__':
    main()
