from datetime import timedelta

class Day:
    '''A day of the week.'''
    def __init__(self, name):
        self.id = -1
        self.week_id = -1
        self.name = name
        self.meals = []
        self.date = None

    def add_meal(self, meal):
        '''Add a meal to the day.'''
        self.meals.append(meal)
        meal.set_day_object(self)

    def set_day_date(self, start_date):
        '''Set the day's date by passing in the start date.'''
        day_name_to_offset = {'Monday': 1, 'Tuesday': 2, 'Wednesday': 3,
                              'Thursday': 4, 'Friday': 5, 'Saturday': 6, 'Sunday': 0}
        self.date = start_date + timedelta(days=day_name_to_offset[self.name])
