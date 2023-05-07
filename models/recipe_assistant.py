from utils.loggerX import Logger
from utils.prompt_factory import PromptFactory

logger = Logger(__name__)

class RecipeAssistant:
    def __init__(self, settings, recommendation_model, recipe_model, recommendation_parser, recipe_parser, recommendation_prompt_template, recipe_prompt_template):
        self.settings = settings
        self.reccomendation_model = recommendation_model
        self.recipe_model = recipe_model
        self.recommendation_parser = recommendation_parser
        self.recipe_parser = recipe_parser
        self.prompt_factory = PromptFactory(self.settings)
        self.recommendation_prompt = recommendation_prompt_template
        self.recipe_prompt = recipe_prompt_template

    def execute_recommendation_prompt(self, prompt_template, query):
        formatted_prompt = prompt_template.format_prompt(query=query)
        output = self.reccomendation_model(formatted_prompt.to_string())
        return output
    
    def execute_recipe_prompt(self, prompt_template, query):
        formatted_prompt = prompt_template.format_prompt(query=query)
        output = self.recipe_model(formatted_prompt.to_string())
        return output    

    def get_recommendation(self, day):
        rec_query = self.prompt_factory.create_recommendation_prompt()
        rec_output = self.execute_recommendation_prompt(self.recommendation_prompt, rec_query)
        recommendation = self.recommendation_parser.parse(rec_output)
        return recommendation

    def get_recipe(self, recommendation):
        ing_query = self.prompt_factory.create_recipe_information_template(recommendation)
        ing_output = self.execute_recipe_prompt(self.recipe_prompt, ing_query)
        recipe = self.recipe_parser.parse(ing_output)
        return recipe