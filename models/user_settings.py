from utils.constants import ValidUserSettings

class UserSettings:
    '''UserSettings class to store user settings'''
    def __init__(self, skill_level, dietary_restrictions, preferences, budget_time_period, budget_amount, option_count, meal_type):
        self.skill_level = skill_level
        self.dietary_restrictions = dietary_restrictions
        self.preferences = preferences
        self.budget_time_period = budget_time_period
        self.budget_amount = budget_amount
        self.option_count = option_count
        self.meal_type = meal_type
        self.day = None

    def __str__(self):
        '''Return a string representation of the UserSettings object'''
        return f'UserSettings({self.skill_level}, {self.dietary_restrictions}, {self.preferences}, {self.budget_time_period}, {self.budget_amount}, {self.option_count}, {self.meal_type}, {self.day})'

    def list_preferences(self):
        '''Apply the user's preferences to the UserSettings object'''
        return ', '.join(self.preferences)

    def list_dietary_restrictions(self):
        '''Apply the user's dietary restrictions to the UserSettings object'''
        return ', '.join(self.dietary_restrictions)

    def to_dict(self):
        '''Return a dictionary representation of the UserSettings object'''
        return {
            ValidUserSettings.OPTION_COUNT: self.option_count,
            ValidUserSettings.MEAL_TYPE: self.meal_type,
            ValidUserSettings.DAY: self.day,
            ValidUserSettings.SKILL_LEVEL: self.skill_level,
            ValidUserSettings.DIETARY_RESTRICTIONS: self.dietary_restrictions,
            ValidUserSettings.PREFERENCES: self.preferences,
            ValidUserSettings.BUDGET_PERIOD: self.budget_time_period,
            ValidUserSettings.BUDGET_AMOUNT: self.budget_amount
        }
