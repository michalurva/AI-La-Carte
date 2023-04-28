class RecipeStore:
    def __init__(self):
        self.recommendations = []
        self.recipes = []

    def add(self, recommendation, recipe):
        self.recommendations.append(recommendation)
        self.recipes.append(recipe)

    def get_all(self):
        return self.recommendations, self.recipes

    def get_recommendation(self, index):
        return self.recommendations[index]

    def get_recipe(self, index):
        return self.recipes[index]

    def clear(self):
        self.recommendations.clear()
        self.recipes.clear()
