from datetime import timedelta
from models.base_entity import BaseEntity
from utils.constants import DayNames
from utils.loggerX import Logger

logger = Logger(__name__)

class Day(BaseEntity):
    '''A day of the week.'''
    table_name = "days"
    def __init__(self, name, db_handler=None):
        super().__init__(db_handler)
        self.week_id = -1
        self.name = name
        self.meals = []
        self.date = None

    @classmethod
    def from_database(cls, database_handler, row_dict):
        name = row_dict['name']
        day = cls(name, database_handler)
        day.id = row_dict['id']
        return day

    def add_meal(self, meal):
        '''Add a meal to the day.'''
        self.meals.append(meal)
        meal.set_day_object(self)

    def set_day_date(self, start_date):
        '''Set the day's date by passing in the start date.'''
        day_name_to_offset = {DayNames.MONDAY: 1, DayNames.TUESDAY: 2, DayNames.WEDNESDAY: 3,
                              DayNames.THURSDAY: 4, DayNames.FRIDAY: 5, DayNames.SATURDAY: 6, DayNames.SUNDAY: 0}
        self.date = start_date + timedelta(days=day_name_to_offset[self.name])

    def to_dict(self) -> dict:
        return {
            'week_id': self.week_id,
            'name': self.name,
            'meals': ",".join(self.meals),
            'date': self.date
        }
