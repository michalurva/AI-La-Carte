import unittest
from datetime import date, timedelta
from models.week import Week
from models.meal import Meal

class TestDates(unittest.TestCase):
    '''Test the Week/Day class's date setting functionality.'''
    def setUp(self):
        self.week = Week()
        self.meal = Meal("Beef and Broccoli Stir-Fry",
                         ["beef", "broccoli", "onion",
                          "garlic", "soy sauce", "oyster sauce",
                          "honey", "jasmine rice"],
                         ["Thinly slice beef, chop broccoli, mince onion and garlic"],
                         30,
                         "Monday")

    def tearDown(self):
        del self.week
        del self.meal

    def test_day_date(self):
        '''Test that the week's dates are set correctly.'''
        today = date.today()
        start_date = today - timedelta(days=today.weekday() + 1)
        for day in self.week.days:
            day_name_to_offset = {'Monday': 1, 'Tuesday': 2, 'Wednesday': 3,
                                  'Thursday': 4, 'Friday': 5, 'Saturday': 6, 'Sunday': 0}
            expected_date = start_date + timedelta(days=day_name_to_offset[day.name])
            self.assertEqual(day.date, expected_date)

    def test_add_meal(self):
        '''Test that a meal can be added to a day.'''
        day_name = "Monday"
        for day in self.week.days:
            if day.name == day_name:
                day.add_meal(self.meal)
                break
        day_meals = None
        for day in self.week.days:
            if day.name == day_name:
                day_meals = day.meals
                break
        self.assertIn(self.meal, day_meals)

if __name__ == '__main__':
    unittest.main()
