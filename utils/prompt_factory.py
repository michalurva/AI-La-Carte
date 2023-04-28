class PromptFactory:
    '''This class is responsible for creating prompts to be sent to the llm.'''
    def __init__(self, user_settings):
        self.skill_level = user_settings.skill_level
        self.dietary_restrictions = user_settings.dietary_restrictions
        self.preferences = user_settings.preferences
        self.budget_time_period = user_settings.budget_time_period
        self.budget_amount = user_settings.budget_amount
        self.option_count = user_settings.option_count
        self.meal_type = user_settings.meal_type
        self.day = user_settings.day

    def prompt_conclusion(self):
        '''Create a prompt to conclude the meal planning session'''
        conclusion_line = "Thank you for your help!"
        return conclusion_line

    def prompt_intro(self):
        """Create a prompt to introduce the meal planning session"""
        intro_line1 = "Hello! I'm trying to help a friend (the cook) plan their meals. I'm hoping you can help me out."
        intro_line2 = "I want to help them plan meals that are delicious (by their own standards)."
        intro_line3 = "It can take a lot of time, effort, and experience to plan meals that are best suited to a person, or family's life and happiness."
        intro_line4 = "Could you please take on the role of a meal planner, so the cook can focus on the things that matter to them!"
        intro_line5 = "And if the cook loves cooking, you can help them foster their passion with creative and inventive ideas."

        return f"{intro_line1}\n{intro_line2}\n{intro_line3}\n{intro_line4}\n{intro_line5}"

    def create_recipe_information_template(self, recommendation):
        '''Create a template for recipe information prompts'''
        prompt = f"Considering the recipe name: {recommendation.recipe_title}, and detailed description: {recommendation.recipe_description}\n \
        Provide a complete recipe, considering all aspects and dishes of the meal:\n \
            -recipe name, ingredients, prep steps, cook steps, cook time, and assigned day.\n \
        This information will be used to create detailed, easy-to-follow recipes for the selected meals"

        return prompt

    def create_recommendation_prompt(self):
        '''Create a prompt for weekday meal options'''
        prompt_intro = self.prompt_intro()
        meal_basics_component = f"Please select {self.option_count} {self.meal_type} options for {self.day}."
        skill_level_component = f"The meal choices, ingredients, cooking techniques, etc. should be tailored to suit a {self.skill_level} cook."
        dietary_restriction_component = f"Please consider the following diet restrictions:{self.dietary_restrictions}"
        food_preferences_component = f"The cook's preferences include:{self.preferences}."
        budget_component = f"The cook is working on a {self.budget_time_period} budget of ${self.budget_amount}."
        prompt = f"{prompt_intro}\n\n{meal_basics_component}\n{skill_level_component}\n{dietary_restriction_component}\n{food_preferences_component}\n{budget_component}\n\n{self.prompt_conclusion()}"

        return prompt
    