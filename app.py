from flask import Flask, render_template, request, redirect, url_for
from flask import current_app
from flask_talisman import Talisman
from flask import jsonify

from foodai import food_ai
from models.recipe_store import RecipeStore
from models.calendar_store import CalendarStore
from utils.constants import CSP, SECRET_KEY
from utils.input_validator import InputValidator

def create_app():
    app = Flask(__name__)
    app.secret_key = SECRET_KEY
    talisman = Talisman(app, content_security_policy=CSP)

    food_ai_service = food_ai()
    recipe_store = RecipeStore()
    calendar_store = CalendarStore()

    app.extensions['food_ai_service'] = food_ai_service
    app.extensions['recipe_store'] = recipe_store
    app.extensions['calendar_store'] = calendar_store

    @app.route('/start_planning', methods=['POST'])
    def start_planning():
        ai_service = current_app.extensions['food_ai_service']
        recommendation, recipe = ai_service.get_recommendation()
        recipe_store.add(recommendation, recipe)
        meal, week = ai_service.save_recipe(recipe)
        calendar_store.add(meal, week)
        # Convert recommendation and recipe objects to dictionaries
        recommendation_dict = recommendation.dict()
        recipe_dict = recipe.dict()
        return jsonify({'recommendation': recommendation_dict, 'recipe': recipe_dict})

    @app.route("/")
    def home():
        return render_template("home.html")

    @app.route('/settings')
    def settings():
        return render_template('settings.html')

    @app.route('/settings2')
    def settings2():
        return render_template('settings2.html')

    @app.route('/planning')
    def planning():
        #TODO add a button to save the recipe
        return render_template('planning.html')

    @app.route('/presenting')
    def presenting():
        return render_template('presenting.html')

    @app.route('/updating', methods=['POST'])
    def updating():
        ai_service = current_app.extensions['food_ai_service']
        calendar_store = current_app.extensions['calendar_store']
        meal = calendar_store.get_meal(-1)
        week = calendar_store.get_week(-1)
        ai_service.create_calendar_event(meal, week)
        return render_template('updating.html')

    @app.route('/submit', methods=['POST'])
    def submit():
        ai_service = current_app.extensions['food_ai_service']
        
        # Get user settings from form
        skill_level = request.form.get('skill_level')
        dietary_restrictions = request.form.getlist('dietary_restrictions')
        preferences = request.form.getlist('preferences')
        budget_time_period = request.form.get('budget_time_period')
        budget_amount = request.form.get('budget_amount')
        num_servings = request.form.get('num_servings')
        meal_type = request.form.get('meal_type')
        day = request.form.get('day')
        
        # Validate the input fields
        if not InputValidator.validate_all(skill_level,
                                        dietary_restrictions,
                                        preferences,
                                        budget_time_period,
                                        budget_amount,
                                        num_servings,
                                        meal_type,
                                        day):
            return redirect(url_for('settings'))
        
        # Configure langchain session
        ai_service.update_user_settings(skill_level,
                                        dietary_restrictions,
                                        preferences,
                                        budget_time_period,
                                        budget_amount,
                                        num_servings,
                                        meal_type)
        
        # Set day
        ai_service.set_day_settings(day)

        return redirect(url_for('planning'))

    @app.route('/recipe', methods=['GET'])
    def recipe():
        recipe_store = current_app.extensions['recipe_store']
        
        recommendation = recipe_store.get_recommendation(-1)
        recipe = recipe_store.get_recipe(-1)
        
        return render_template('recipe.html', recommendation=recommendation, recipe=recipe)

    return app

if __name__ == "__main__":
    app = create_app()
    app.run(host="0.0.0.0", port=5000, debug=True)
