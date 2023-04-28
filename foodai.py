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
from utils.loggerX import Logger


logger = Logger(__name__)

class food_ai():
    def __init__(self):
        self.model = OpenAI(model_name='text-davinci-003', temperature=0.5, max_tokens=1024)
        self.db_handler = DatabaseHandler()
        self.user_settings = None
        
    def update_user_settings(self, skill_level, dietary_restrictions, preferences, budget_time_period, budget_amount, option_count, meal_type):
        self.user_settings = UserSettings(
            skill_level=skill_level,
            dietary_restrictions=dietary_restrictions,
            preferences=preferences,
            budget_time_period=budget_time_period,
            budget_amount=budget_amount,
            option_count=option_count,
            meal_type=meal_type,
        )
        
    def set_day_settings(self, day):
        self.user_settings.day = day
        
    def get_recommendation(self):
        if self.user_settings is None:
            raise Exception("User settings not set")

        # Set up parsers
        recipe_parser = PydanticOutputParser(pydantic_object=Recipe)
        recommendation_parser = PydanticOutputParser(pydantic_object=Recommendation)
        # Set up prompts
        recommendation_prompt = RecipePromptTemplate(recommendation_parser)
        recipe_prompt = RecipePromptTemplate(recipe_parser)
        # Set up assistant
        assistant = RecipeAssistant(self.user_settings,
                                    self.model,
                                    recommendation_parser,
                                    recipe_parser,
                                    recommendation_prompt,
                                    recipe_prompt)
        
        logger.info("_______________user_settings_______________")
        logger.info(self.user_settings.__str__())
        
        # Get recommendation
        recommendation = assistant.get_recommendation(self.user_settings.day)
        logger.info("_______________recommendation_______________")
        logger.info(recommendation)
        logger.info("____________________________________________")
        # Get recipe
        recipe = assistant.get_recipe(recommendation)
        logger.info("_________________recipe_____________________")
        logger.info(recipe)
        logger.info("____________________________________________")
        
        return recommendation, recipe
        
    def save_recipe(self, recipe):
        # Create meal, day, and week objects
        meal = Meal(recipe.recipe_title,
                    recipe.ingredients,
                    recipe.prep_steps,
                    recipe.cook_time,
                    recipe.day,
                    db_handler=self.db_handler)
        day = Day("Tuesday", db_handler=self.db_handler)
        week = Week(db_handler=self.db_handler)
        # Add meal to day and day to week
        day.add_meal(meal)
        week.tue = day
        week.set_week_dates()
        #TODO save to database
        
    # def submit():
        # # Set up database
        # db_handler = DatabaseHandler()
        # # Set user settings
        # settings = UserSettings(
        #     skill_level="experienced",
        #     dietary_restrictions="None",
        #     preferences="Italian, Mexican, Chinese, American, Korean, Japanese, Greek, French",
        #     budget = "extravagant daily budget of $50",
        #     option_count="one",
        #     meal_type="weeknight dinner",
        # )
        # settings.day = "Tuesday"
        
        # # Set up llm
        # model = OpenAI(model_name='text-davinci-003', temperature=0.5, max_tokens=1024)
        # # Set up parsers
        # recipe_parser = PydanticOutputParser(pydantic_object=Recipe)
        # recommendation_parser = PydanticOutputParser(pydantic_object=Recommendation)
        # # Set up prompts
        # recommendation_prompt = RecipePromptTemplate(recommendation_parser)
        # recipe_prompt = RecipePromptTemplate(recipe_parser)
        # # Set up assistant
        # assistant = RecipeAssistant(settings,
        #                             model,
        #                             recommendation_parser,
        #                             recipe_parser,
        #                             recommendation_prompt,
        #                             recipe_prompt)
        # # Get recommendation
        # recommendation = assistant.get_recommendation("Sunday")
        # print("_______________recommendation_______________")
        # print(recommendation)
        # print("____________________________________________")
        # # Get recipe
        # recipe = assistant.get_recipe(recommendation)
        # print("_________________recipe_____________________")
        # print(recipe)
        # print("____________________________________________")

        # Create meal, day, and week objects
        # meal = Meal(recipe.recipe_title, recipe.ingredients, recipe.prep_steps, recipe.cook_time, recipe.day, db_handler=db_handler)
        # day = Day("Tuesday", db_handler=db_handler)
        # week = Week(db_handler=db_handler)
        # # Add meal to day and day to week
        # day.add_meal(meal)
        # week.tue = day
        # week.set_week_dates()

    def create_calendar_event(meal, week):
        # Save meal to calendar
        client = GoogleCalendarClient("credentials.json", "token.json", scopes=["https://www.googleapis.com/auth/calendar"])
        client.create_meal_event(meal, week.start_date)