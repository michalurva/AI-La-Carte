from wtforms import Form, StringField, SelectField, IntegerField, BooleanField, validators

class SettingsForm(Form):
    skill_level = SelectField('Skill Level', choices=[('Beginner', 'Beginner'), ('Intermediate', 'Intermediate'), ('Experienced', 'Experienced'), ('Expert', 'Expert')])
    dietary_restrictions = BooleanField('Dairy-free')
    dietary_restrictions = BooleanField('Gluten-free')
    dietary_restrictions = BooleanField('Keto')
    dietary_restrictions = BooleanField('Peanut-free')
    dietary_restrictions = BooleanField('Pescetarian')
    dietary_restrictions = BooleanField('Shellfish-free')
    dietary_restrictions = BooleanField('Vegan')
    dietary_restrictions = BooleanField('Vegetarian')
    preferences = BooleanField('American')
    budget_time_period = StringField('Budget Time Period', [validators.Length(min=1, max=50)])
    budget_amount = IntegerField('Budget Amount', [validators.NumberRange(min=1)])
    num_servings = IntegerField('Servings', [validators.NumberRange(min=1, max=6)])
    meal_type = StringField('Meal Type', [validators.Length(min=1, max=50)])
    day = StringField('Day', [validators.Length(min=1, max=50)])
