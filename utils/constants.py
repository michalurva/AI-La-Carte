from enum import Enum

AI_MODEL_DAVINCI_003 = "text-davinci-003"
CREDENTIALS_FILE = ""
LOG_FILE = "C:\\Users\\mgarc\\PythonLogs\\MealPlanner\\log.txt"
DATABASE_FILE = "data\\test_db_handler_2.db"
GOOGLE_CREDENTIALS_FILE = "C:\Users\mgarc\PythonCreds\MealPlanner\credentials.json"
GOOGLE_TOKEN_FILE = "C:\Users\mgarc\PythonCreds\MealPlanner\token.json"

# Test Constants
TEST_BASE_ENTITY_DB_FILE = "tests/test_data/test_base_entity.db"
TEST_DB_HANDLER_FILE = "tests/test_data/test_database_handler.db"
TEST_DAY_DB_FILE = "tests/test_data/test_day.db"
TEST_MEALS_CSV_FILE = "tests/test_data/test_meals.csv"
TEST_SAVED_MEALS_CSV_FILE = "tests/test_data/test_saved_meals.csv"
TEST_CALENDAR_CSV_FILE = "tests/test_data/test_calendar_csv"

class DayNames(Enum):
    SUNDAY = "Sunday"
    MONDAY = "Monday"
    TUESDAY = "Tuesday"
    WEDNESDAY = "Wednesday"
    THURSDAY = "Thursday"
    FRIDAY = "Friday"
    SATURDAY = "Saturday"
    SUN = "sun"    
    MON = "mon"
    TUE = "tue"
    WED = "wed"
    THU = "thu"
    FRI = "fri"
    SAT = "sat"

    @classmethod
    def to_list(cls):
        return [day.value for day in cls]

    @classmethod
    def to_string(cls):
        return ", ".join(cls.to_list())

    @classmethod
    def to_dict(cls):
        return {day.name: day.value for day in cls}
    
#FRONT-END CONSTANTS
class ValidUserSettings(Enum):
    OPTION_COUNT = "option_count"
    MEAL_TYPE = "meal_type"
    DAY = "day"
    SKILL_LEVEL = "skill_level"
    DIETARY_RESTRICTIONS = "dietary_restrictions"
    PREFERENCES = "preferences"
    BUDGET_PERIOD = "budget_period"
    BUDGET_AMOUNT = "budget_amount"