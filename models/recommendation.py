from pydantic import BaseModel, Field

class Recommendation(BaseModel):
    recipe_title: str
    recipe_description: str