from datetime import date, timedelta
from models.base_entity import BaseEntity
from utils.loggerX import Logger

logger = Logger(__name__)

class Week(BaseEntity):
    '''Week class for storing a week's worth of days.'''
    table_name = "weeks"
    def __init__(self, start_date=None, db_handler=None):
        super().__init__(db_handler)
        self.start_date = start_date or date.today().isoformat()
        self.sun = None
        self.mon = None
        self.tue = None
        self.wed = None
        self.thu = None
        self.fri = None
        self.sat = None

    @classmethod
    def from_database(cls, database_handler, row_dict):
        '''Create a new object from a database row.'''
        start_date = row_dict['start_date']
        week = cls(start_date, database_handler)
        week.id = row_dict['id']
        week.sun = row_dict['sun']
        week.mon = row_dict['mon']
        week.tue = row_dict['tue']
        week.wed = row_dict['wed']
        week.thu = row_dict['thu']
        week.fri = row_dict['fri']
        week.sat = row_dict['sat']
        logger.debug("week loaded")
        return week

    def get_days_list(self):
        '''Get the week's days.'''
        return [self.sun, self.mon, self.tue, self.wed, self.thu, self.fri, self.sat]

    def set_week_dates(self, start_date=None):
        '''Set the week's dates by passing in the start date.'''
        if start_date is None:
            today = date.today()
            #Calculate the Sunday of the current week
            start_date = today - timedelta(days=today.weekday() + 1)
        for day in self.get_days_list():
            if day is not None:
                day.set_day_date(start_date)

    # def update_day(self, day):
    #     '''Update a day's meal.'''
    #     if _day.name == day.name:
    #         _day = day

    def to_dict(self) -> dict:
        '''Convert the object's properties to a dictionary.'''
        return {
                'start_date': self.start_date,
                'sun': self.sun,
                'mon': self.mon,
                'tue': self.tue,
                'wed': self.wed,
                'thu': self.thu,
                'fri': self.fri,
                'sat': self.sat
                }
