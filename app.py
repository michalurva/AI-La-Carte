from flask import Flask, render_template, request, redirect, url_for
from flask import current_app
from foodai import food_ai
from models.recipe_store import RecipeStore

app = Flask(__name__)

food_ai_service = food_ai()
recipe_store = RecipeStore()

app.extensions['food_ai_service'] = food_ai_service
app.extensions['recipe_store'] = recipe_store

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
    ai_service = current_app.extensions['food_ai_service']
    recipe_store = current_app.extensions['recipe_store']
    recommendation, recipe = ai_service.get_recommendation()
    ai_service.save_recipe(recipe)
    recipe_store.add(recommendation, recipe)
    #TODO plug in routing to recipe page and persist the recommendations/recipes
    #TODO add a button to save the recipe
    return render_template('planning.html')

@app.route('/presenting')
def presenting():
    return render_template('presenting.html')

@app.route('/updating')
def updating():
    ai_service = current_app.extensions['food_ai_service']
    return render_template('updating.html')

@app.route('/submit', methods=['POST'])
def submit():
    ai_service = current_app.extensions['food_ai_service']
    
    # Get user settings from form
    skill_level = request.form.get('skill_level')
    dietary_restrictions = request.form.get('dietary_restrictions')
    preferences = request.form.get('preferences')
    budget_time_period = request.form.get('budget_time_period')
    budget_amount = request.form.get('budget_amount')
    option_count = request.form.get('option_count')
    meal_type = request.form.get('meal_type')
    day = request.form.get('day')
    
    # Configure langchain session
    ai_service.update_user_settings(skill_level,
                                    dietary_restrictions,
                                    preferences,
                                    budget_time_period,
                                    budget_amount,
                                    option_count,
                                    meal_type)
    # Set day
    ai_service.set_day_settings(day)

    return redirect(url_for('planning'))

@app.route('/recipe', methods=['GET'])
def recipe():
    recipe_store = current_app.extensions['recipe_store']
    
    recommendation = recipe_store.get_recommendation(-1)
    recipe = recipe_store.get_recipe(-1)
    
    return render_template('recipe.html')

if __name__ == "__main__":
    app.run(debug=True)
