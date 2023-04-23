from api.google_api_calendar_client import GoogleCalendarClient
from langchain.llms import OpenAI
from langchain.output_parsers import PydanticOutputParser
from models.recipe_assistant import RecipeAssistant
from models.user_settings import UserSettings
from models.prompt_template import RecipePromptTemplate
from models.recipe import Recipe
from models.recommendation import Recommendation
from models.meal import Meal
from models.day import Day
from models.week import Week
from utils.database_handler import DatabaseHandler
from utils.calendar_csv_handler import CalendarCSVHandler
from utils.loggerX import Logger


logger = Logger(__name__)

def test_2():
    # Set up database
    db_handler = DatabaseHandler()
    csv_handler = CalendarCSVHandler()
    # Set user settings
    settings = UserSettings(
        skill_level="experienced",
        dietary_restrictions="None",
        preferences="Italian, Mexican, Chinese, American, Korean, Japanese, Greek, French",
        budget = "extravagant daily budget of $50",
        option_count="one",
        meal_type="weeknight dinner",
    )
    settings.day = "Tuesday"
    
    # Set up llm
    model = OpenAI(model_name='text-davinci-003', temperature=0.5, max_tokens=1024)
    # Set up parsers
    recipe_parser = PydanticOutputParser(pydantic_object=Recipe)
    recommendation_parser = PydanticOutputParser(pydantic_object=Recommendation)
    # Set up prompts
    recommendation_prompt = RecipePromptTemplate(recommendation_parser)
    recipe_prompt = RecipePromptTemplate(recipe_parser)
    # Set up assistant
    assistant = RecipeAssistant(settings,
                                model,
                                recommendation_parser,
                                recipe_parser,
                                recommendation_prompt,
                                recipe_prompt)
    # Get recommendation
    recommendation = assistant.get_recommendation("Sunday")
    print("_______________recommendation_______________")
    print(recommendation)
    print("____________________________________________")
    # Get recipe
    recipe = assistant.get_recipe(recommendation)
    print("_________________recipe_____________________")
    print(recipe)
    print("____________________________________________")

    # Create meal, day, and week objects
    meal = Meal(recipe.recipe_title, recipe.ingredients, recipe.prep_steps, recipe.cook_time, recipe.day, db_handler=db_handler)
    day = Day("Tuesday", db_handler=db_handler)
    week = Week(db_handler=db_handler)
    # Add meal to day and day to week
    day.add_meal(meal)
    week.tue = day
    week.set_week_dates()

    # Save meal to calendar
    client = GoogleCalendarClient("credentials.json", "token.json", scopes=["https://www.googleapis.com/auth/calendar"])
    client.create_meal_event(meal, week.start_date)

if __name__ == "__main__":
    test_2()