class CalendarStore:
    def __init__(self):
        self.meals = []
        self.weeks = []

    def add(self, recommendation, recipe):
        self.meals.append(recommendation)
        self.weeks.append(recipe)

    def get_all(self):
        return self.meals, self.weeks

    def get_meal(self, index):
        return self.meals[index]

    def get_week(self, index):
        return self.weeks[index]

    def clear(self):
        self.meals.clear()
        self.weeks.clear()
