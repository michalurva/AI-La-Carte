from typing import List
from pydantic import BaseModel, Field, validator

class Recipe(BaseModel):
    recipe_title: str = Field(description="The title of the recipe")
    ingredients: List[str] = Field(description="list of all ingredients")
    prep_steps: List[str] = Field(description="list of all prep steps")
    cook_steps: List[str] = Field(description="list of all cook steps")
    cook_time: int = Field(description="cook time in minutes")
    day: str = Field(description="day of the week for which selected meal is assigned")

    # @validator('prep_steps', 'cook_steps', pre=True)
    # def split_instruction_lines(cls, value):
    #     return value.split('.') if value else []

    # @validator('ingredients', pre=True)
    # def split_ingredient_lines(cls, value):
    #     return value.split(',') if value else []
