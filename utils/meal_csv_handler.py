import csv
from typing import List
from models.meal import Meal

class MealCSVHandler:
    '''Handles CSV operations for meals.'''
    @staticmethod
    def load_from_csv(file_path: str) -> List[Meal]:
        '''Load meals from a CSV file.'''
        meals = []
        with open(file_path, 'r', encoding="UTF-8") as csvfile:
            csv_reader = csv.DictReader(csvfile)
            for row in csv_reader:
                meal = Meal(row["name"],
                            row["ingredients"].split(';'),
                            row["prep_steps"].split(';'),
                            int(row["cook_time"]),
                            row["day_of_week"])
                meal.protein = row["protein"]
                meals.append(meal)
        return meals

    @staticmethod
    def save_to_csv(meals: List[Meal], file_path: str):
        '''Save meals to a CSV file. Adds id'''
        with open(file_path, 'w', newline='', encoding="UTF-8") as csvfile:
            fieldnames = ['name', 'ingredients', 'prep_steps',
                          'cook_time', 'protein', "day_of_week"]
            csv_writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
            csv_writer.writeheader()

            for meal in meals:
                csv_writer.writerow({
                    'name': meal.name,
                    'ingredients': ';'.join(meal.ingredients),
                    'prep_steps': ';'.join(meal.prep_steps),
                    'cook_time': meal.cook_time,
                    'protein': meal.protein,
                    'day_of_week': meal.day_id,
                })
