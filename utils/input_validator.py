from enum import Enum
from flask import flash

class InputValidator:
    @staticmethod
    def validate_skill_level(skill_level):
        return skill_level in (level.value for level in ValidSkillLevel)

    @staticmethod
    def validate_dietary_restrictions(dietary_restrictions):
        return all(restriction in (dr.value for dr in ValidDietaryRestrictions) for restriction in dietary_restrictions)

    @staticmethod
    def validate_preferences(preferences):
        return all(preference in (p.value for p in ValidPreferences) for preference in preferences)

    @staticmethod
    def validate_budget_time_period(budget_time_period):
        return budget_time_period in (period.value for period in ValidBudgetPeriod)

    @staticmethod
    def validate_budget_amount(budget_amount):
        try:
            float(budget_amount)
            return True
        except ValueError:
            return False

    @staticmethod
    def validate_option_count(option_count):
        return option_count in (count.value for count in ValidOptionCount)

    @staticmethod
    def validate_meal_type(meal_type):
        return meal_type in (mt.value for mt in ValidMealType)

    @staticmethod
    def validate_day(day):
        return day in (d.value for d in ValidDays)

    @classmethod
    def validate_all(cls, skill_level, dietary_restrictions, preferences, budget_time_period, budget_amount, option_count, meal_type, day):
        if not cls.validate_skill_level(skill_level):
            flash("Invalid skill level")
            return False

        if not cls.validate_dietary_restrictions(dietary_restrictions):
            flash("Invalid dietary restrictions")
            return False

        if not cls.validate_preferences(preferences):
            flash("Invalid preferences")
            return False

        if not cls.validate_budget_time_period(budget_time_period):
            flash("Invalid budget time period")
            return False

        if not cls.validate_budget_amount(budget_amount):
            flash("Invalid budget amount")
            return False

        if not cls.validate_option_count(option_count):
            flash("Invalid option count")
            return False

        if not cls.validate_meal_type(meal_type):
            flash("Invalid meal type")
            return False

        if not cls.validate_day(day):
            flash("Invalid day")
            return False

        return True

class ValidUserSettings(Enum):
    OPTION_COUNT = "option_count"
    MEAL_TYPE = "meal_type"
    DAY = "day"
    SKILL_LEVEL = "skill_level"
    DIETARY_RESTRICTIONS = "dietary_restrictions"
    PREFERENCES = "preferences"
    BUDGET_PERIOD = "budget_period"
    BUDGET_AMOUNT = "budget_amount"
    
class ValidSkillLevel(Enum):
    BEGINNER = "Beginner"
    INTERMEDIATE = "Intermediate"
    ADVANCED = "Experienced"
    EXPERT = "Expert"
    
class ValidDays(Enum):
    SUNDAY = "Sunday"
    MONDAY = "Monday"
    TUESDAY = "Tuesday"
    WEDNESDAY = "Wednesday"
    THURSDAY = "Thursday"
    FRIDAY = "Friday"
    SATURDAY = "Saturday"
    
class ValidDietaryRestrictions(Enum):
    DAIRY_FREE = "Dairy-free"
    GLUTEN_FREE = "Gluten-free"
    KETO = "Keto"
    PEANUT_FREE = "Peanut-free"
    PESCETARIAN = "Pescetarian"
    SHELLFISH_FREE = "Shellfish-free"
    VEGAN = "Vegan"
    VEGETARIAN = "Vegetarian"
    
class ValidPreferences(Enum):
    AMERICAN = "American"
    CHINESE = "Chinese"
    FILIPINO = "Filipino"
    ITALIAN = "Italian"
    JAPANESE = "Japanese"
    KOREAN = "Korean"
    MEXICAN = "Mexican"
    SPANISH = "Spanish"
    THAI = "Thai"
    
class ValidBudgetPeriod(Enum):
    DAILY = "Daily"
    WEEKLY = "Weekly"
    MONTHLY = "Monthly"
    YEARLY = "Yearly"
    
class ValidOptionCount(Enum):
    ONE = "1"
    TWO = "2"
    THREE = "3"
    
class ValidMealType(Enum):
    BREAKFAST = "Breakfast"
    LUNCH = "Lunch"
    WEEKNIGHT_DINNER = "Weeknight Dinner"
    WEEKEND_DINNER = "Weekend Dinner"
    SNACK = "Snack"
