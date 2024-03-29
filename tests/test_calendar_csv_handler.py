import csv
import os
import unittest

from models.day import Day
from models.meal import Meal
from models.week import Week

from utils.calendar_csv_handler import CalendarCSVHandler
from utils.constants import *
from utils.loggerX import Logger

logger = Logger(__name__)

class TestCalendarCSVHandler(unittest.TestCase):
    '''Test CalendarCSVHandler class.'''
    def setUp(self):
        self.week = Week()
        self.test_meals = [
            Meal("Beef and Broccoli Stir-Fry",
                 ["beef", "broccoli", "onion", "garlic",
                  "soy sauce", "oyster sauce", "honey", "jasmine rice"],
                 ["Thinly slice beef, chop broccoli, mince onion and garlic"],
                 30,
                 "Monday")
        ]

        self.week.mon = Day(DayNames.MONDAY)
        self.week.tue = Day(DayNames.TUESDAY)
        self.week.wed = Day(DayNames.WEDNESDAY)
        self.week.thu = Day(DayNames.THURSDAY)
        self.week.fri = Day(DayNames.FRIDAY)
        self.week.mon.add_meal(self.test_meals[0])
        self.week.tue.add_meal(self.test_meals[0])
        self.week.wed.add_meal(self.test_meals[0])
        self.week.thu.add_meal(self.test_meals[0])
        self.week.fri.add_meal(self.test_meals[0])
        self.week.set_week_dates()
        self.file_path = TEST_CALENDAR_CSV_FILE

    def tearDown(self):
        if os.path.exists(self.file_path):
            os.remove(self.file_path)

    def test_save_to_csv(self):
        '''Test save_to_csv method.'''
        CalendarCSVHandler.save_to_csv(self.week, self.file_path)
        self.assertTrue(os.path.exists(self.file_path))

        with open(self.file_path, 'r', newline='', encoding="UTF-8") as csvfile:
            csv_reader = csv.DictReader(csvfile)
            fieldnames = csv_reader.fieldnames
            self.assertEqual(fieldnames, ['Subject', 'Start Date', 'Start Time',
                                          'End Date', 'End Time',
                                          'All Day Event', 'Description',
                                          'Location', 'Private'])

            for row in csv_reader:
                self.assertEqual(row['Subject'], f'{self.test_meals[0].name} (Cooking)')
                self.assertEqual(row['All Day Event'], 'False')
                self.assertEqual(
                    row['Description'],
                    f'Cook {self.test_meals[0].name} for {self.test_meals[0].cook_time} minutes')
                self.assertEqual(row['Private'], 'True')
                logger.debug(f'row: {row}')

if __name__ == '__main__':
    unittest.main()
