from typing import List
from pydantic import BaseModel, Field

class Recipe(BaseModel):
    recipe_title: str = Field(description="The title of the recipe")
    ingredients: List[str] = Field(description="list of all ingredients")
    prep_steps: List[str] = Field(description="list of all prep steps")
    cook_steps: List[str] = Field(description="list of all cook steps")
    cook_time: int = Field(description="cook time in minutes")
    day: str = Field(description="day of the week for which selected meal is assigned")
