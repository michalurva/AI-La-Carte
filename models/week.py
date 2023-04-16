from datetime import date, timedelta
from models.day import Day

class Week:
    '''Week class for storing a week's worth of meals.'''
    def __init__(self, start_date=None):
        self.id = -1
        self.days = [Day(day) for day in ['Monday', 'Tuesday', 'Wednesday',
                                          'Thursday', 'Friday', 'Saturday', 'Sunday']]
        self.sun = self.days[0]
        self.mon = self.days[1]
        self.tue = self.days[2]
        self.wed = self.days[3]
        self.thu = self.days[4]
        self.fri = self.days[5]
        self.sat = self.days[6]
        self.set_week_dates(start_date)

    def set_week_dates(self, start_date=None):
        '''Set the week's dates by passing in the start date.'''
        if start_date is None:
            today = date.today()
            # Calculate the Sunday of the current week
            start_date = today - timedelta(days=today.weekday() + 1)
        for day in self.days:
            day.set_day_date(start_date)

    def update_day(self, day):
        '''Update a day's meal.'''
        for _day in self.days:
            if _day.name == day.name:
                _day = day
