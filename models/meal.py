# Standardize meal data format
class Meal:
    """Meal class for storing meal data."""

    def __init__(self, name, ingredients, prep_steps, cook_time, day_name):
        self.id = -1
        self.name = name
        self.ingredients = ingredients
        self.prep_steps = prep_steps
        self.cook_time = cook_time
        self.protein = self.identify_protein()
        self.day_name = day_name
        self.day_object = None

    def identify_protein(self):
        '''Identify the protein in the meal. Used to schedule defrosting.'''
        proteins = ("beef", "chicken", "pork", "fish", "tofu", "eggs", "cheese")
        for ingredient in self.ingredients:
            for word in ingredient.split():
                if word in proteins:
                    return word

    def set_day_object(self, day_object):
        '''Set the day object.'''
        self.day_object = day_object

    def __str__(self):
        return f"{self.name} ({self.cook_time} minutes) - Protein: {self.protein}"

def test():
    '''Test the Meal class.'''
    # Example meals for testing
    meals = [Meal("Beef and Broccoli Stir-Fry",
                  ["beef", "broccoli", "onion",
                   "garlic", "soy sauce", "oyster sauce",
                   "honey", "jasmine rice"],
                  ["Thinly slice beef, chop broccoli, mince onion and garlic"],
                  30,
                  "Monday"),
             # Add more example meals...
            ]

    assert meals[0].protein == "beef", "Expected protein: beef"
