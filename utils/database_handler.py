import sqlite3
from typing import List, Optional
from models.meal import Meal
from models.day import Day
from models.week import Week

class DatabaseHandler:
    """handles database operations for meals."""

    def __init__(self, db_name: str = "meal_planner.db"):
        self.db_name = db_name
        self.db_conn = None
        self._initialize_database()

    def _initialize_database(self):

        with sqlite3.connect(self.db_name) as conn:
            cursor = conn.cursor()
            cursor.execute("""
            CREATE TABLE IF NOT EXISTS meals (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT NOT NULL,
                ingredients TEXT NOT NULL,
                prep_steps TEXT NOT NULL,
                cook_time INTEGER NOT NULL,
                protein TEXT NOT NULL,
                day TEXT
            )
            """)

            cursor.execute("""
            CREATE TABLE IF NOT EXISTS days (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                week_id INTEGER,
                name TEXT NOT NULL
            )
            """)

            cursor.execute("""
            CREATE TABLE IF NOT EXISTS weeks (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                sun INTEGER,
                mon INTEGER,
                tue INTEGER,
                wed INTEGER,
                thu INTEGER,
                fri INTEGER,
                sat INTEGER
            )
            """)
            conn.commit()
            self.db_conn = conn

    def create_day(self, day: Day) -> Day:
        '''Create a day in the database.'''
        with self.db_conn as conn:
            cursor = conn.cursor()
            cursor.execute("""
            INSERT INTO days (week_id, name)
            VALUES (?, ?)
            """, (day.week_id, day.name))
            conn.commit()
            day.id = cursor.lastrowid
            return day

    def update_day(self, day: Day) -> Day:
        '''Update a day in the database.'''
        with self.db_conn as conn:
            cursor = conn.cursor()
            cursor.execute("""
            UPDATE days
            SET week_id = ?, name = ?
            WHERE id = ?
            """, (day.week_id, day.name, day.id))            
            conn.commit()
            day.id = cursor.lastrowid
            return day

    def read_day(self, day_id: int) -> Optional[Day]:
        '''Read a day from the database.'''
        with self.db_conn as conn:
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM days WHERE id = ?", (day_id,))
            row = cursor.fetchone()
            if row:
                day = Day(row[1])
                return day
            else:
                return None


    def create_week(self, week: Week) -> Week:
        '''Create a week in the database.'''
        with self.db_conn as conn:
            cursor = conn.cursor()
            cursor.execute("""
            INSERT INTO weeks DEFAULT VALUES
            """)
            conn.commit()
            week_id = cursor.lastrowid
            for day in week.days:
                day.week_id = week_id  # Add this line to set week_id for each Day object before creating it
                day = self.create_day(day)
                cursor.execute("""
                UPDATE days
                SET week_id = ?
                WHERE id = ?
                """, (day.week_id, day.id))
            conn.commit()
            week.id = week_id
            return self.update_week(week)

    def update_week(self, week: Week) -> Week:
        '''Update a week in the database.'''
        with self.db_conn as conn:
            cursor = conn.cursor()
            cursor.execute("""
            UPDATE weeks
            SET sun = ?, mon = ?, tue = ?, wed = ?, thu = ?, fri = ?, sat = ?
            WHERE id = ?
            """,
            (week.sun.id, week.mon.id, week.tue.id, week.wed.id, week.thu.id, week.fri.id, week.sat.id,
             week.id))
            conn.commit()
            return week

    def read_week(self, week: Week) -> Optional[Week]:
        '''Read a week from the database.'''
        with self.db_conn as conn:
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM weeks WHERE id = ?", (week.id,))
            row = cursor.fetchone()
            if row:
                week = Week()
                week.id = row[0]
                cursor.execute("SELECT * FROM days WHERE week_id = ?", (week.id,))
                rows = cursor.fetchall()
                for row in rows:
                    day = self.read_day(row[0])
                    week.update_day(day)
                return week
            else:
                return None

    def create_meal(self, meal: Meal) -> Meal:
        '''Create a meal in the database.'''
        with self.db_conn as conn:
            cursor = conn.cursor()
            cursor.execute("""
            INSERT INTO meals (name, ingredients, prep_steps, cook_time, protein, day)
            VALUES (?, ?, ?, ?, ?, ?)
            """, (meal.name, ','.join(meal.ingredients), ';'.join(meal.prep_steps),
                meal.cook_time, meal.protein, meal.day_id))
            conn.commit()
            meal.id = cursor.lastrowid
            return meal

    def read_meal(self, meal_id: int) -> Optional[Meal]:
        """Get a meal from the database by id."""
        with self.db_conn as conn:
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM meals WHERE id = ?", (meal_id,))
            row = cursor.fetchone()
            if row:
                meal = Meal(row[1], row[2].split(','), row[3].split(';'), row[4], row[6])
                meal.id = row[0]
                meal.protein = row[5]
                return meal
            else:
                return None

    def read_all_meals(self) -> List[Meal]:
        """Get all meals from the database."""
        meals = []
        with self.db_conn as conn:
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM meals")
            rows = cursor.fetchall()
            for row in rows:
                meal = Meal(row[1], row[2].split(','), row[3].split(';'), row[4], row[6])
                meal.id = row[0]
                meal.protein = row[5]
                meals.append(meal)
        return meals

    def update_meal(self, meal: Meal) -> bool:
        """Update a meal in the database."""
        with self.db_conn as conn:
            cursor = conn.cursor()
            cursor.execute("""
            UPDATE meals
            SET name = ?, ingredients = ?, prep_steps = ?, cook_time = ?, protein = ?, day = ?
            WHERE id = ?
            """, (meal.name, ','.join(meal.ingredients), ';'.join(meal.prep_steps),
                  meal.cook_time, meal.protein, meal.day_object.id, meal.id))
            conn.commit()
            return cursor.lastrowid == meal.id

    def delete_meal(self, meal: Meal) -> bool:
        """Delete a meal from the database."""
        with self.db_conn as conn:
            cursor = conn.cursor()
            cursor.execute("DELETE FROM meals WHERE id = ?", (meal.id,))
            conn.commit()
            return cursor.rowcount == meal.id

    def delete_week(self, week: Week) -> bool:
        """Delete a week from the database."""
        with self.db_conn as conn:
            cursor = conn.cursor()
            cursor.execute("DELETE FROM weeks WHERE id = ?", (week.id,))
            conn.commit()
            return cursor.rowcount == week.id

    def delete_day(self, day: Day) -> bool:
        """Delete a day from the database."""
        with self.db_conn as conn:
            cursor = conn.cursor()
            cursor.execute("DELETE FROM days WHERE id = ?", (day.id,))
            conn.commit()
            return cursor.rowcount == day.id

    def drop_tables(self):
        '''clean up the database'''
        with self.db_conn as conn:
            cursor = conn.cursor()
            cursor.execute("DROP TABLE IF EXISTS days")
            cursor.execute("DROP TABLE IF EXISTS meals")
            cursor.execute("DROP TABLE IF EXISTS weeks")
            conn.commit()
            conn.close()

def test():
    """Test the database handler."""
    db_handler = DatabaseHandler()

    test_week = Week()

    # Create a new meal in the database
    new_meal_id = db_handler.create_meal(
        Meal("Beef and Broccoli Stir-Fry",
             [
              "beef", "broccoli", "onion", "garlic",
              "soy sauce", "oyster sauce", "honey",
              "jasmine rice"
             ],
             ["Thinly slice beef, chop broccoli, mince onion and garlic"],
             30,
             test_week.days[0],
            )
        )

    # Read a meal from the database
    meal_from_db = db_handler.read_meal(new_meal_id)
    print(meal_from_db.name)

    # Update a meal in the database
    meal_from_db.cook_time = 35
    db_handler.update_meal(meal_from_db)

    # Read all meals from the database
    all_meals = db_handler.read_all_meals()
    for meal in all_meals:
        print(meal.name)

    # Delete a meal from the database
    db_handler.delete_meal(new_meal_id)
