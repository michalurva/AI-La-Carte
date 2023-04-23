class UserSettings:
    '''UserSettings class to store user settings'''
    def __init__(self, skill_level, dietary_restrictions, preferences, budget, option_count, meal_type):
        self.skill_level = skill_level
        self.dietary_restrictions = dietary_restrictions
        self.preferences = preferences
        self.budget = budget
        self.option_count = option_count
        self.meal_type = meal_type
        self.day = None

    def __str__(self):
        '''Return a string representation of the UserSettings object'''
        return f'UserSettings({self.skill_level}, {self.dietary_restrictions}, {self.preferences}, {self.budget}, {self.option_count}, {self.meal_type})'

    def apply_preferences(self, preferences_list):
        '''Apply the user's preferences to the UserSettings object'''
        self.preferences = '-'.join(preferences_list)

    def apply_dietary_restrictions(self, dietary_restrictions_list):
        '''Apply the user's dietary restrictions to the UserSettings object'''
        self.dietary_restrictions = ','.join(dietary_restrictions_list)

    def apply_skill_level(self, skill_level):
        '''Apply the user's skill level to the UserSettings object'''
        self.skill_level = skill_level

    def apply_budget(self, budget):
        '''Apply the user's budget to the UserSettings object'''
        self.budget = budget

    def to_dict(self):
        '''Return a dictionary representation of the UserSettings object'''
        return {
            "option_count": self.option_count,
            "meal_type": self.meal_type,
            "day": "Monday",
            "skill_level": self.skill_level,
            "dietary_restrictions": self.dietary_restrictions,
            "preferences": self.preferences,
            "budget_status": self.budget["status"],
            "budget_period": self.budget["period"],
            "budget_amount": self.budget["amount"]
        }

user_settings_to_dict = {
    'skill_level': 'beginner',
    'dietary_restrictions': 'vegetarian',
    'preferences': 'Italian',
    'budget': 'moderate',
    'option_count': 'three',
    'meal_type': 'weeknight dinner'
}
