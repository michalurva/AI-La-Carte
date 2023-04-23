from pydantic import BaseModel, Field, validator

class Recommendation(BaseModel):
    recipe_title: str = Field(description="mouth-watering title of the recipe")
    recipe_description: str = Field(description="mouth-watering description of the meal")