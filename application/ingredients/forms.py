from flask_wtf import FlaskForm
from wtforms import StringField, validators, SelectField, SubmitField, ValidationError
from application.ingredients.models import Ingredient

def ingredient_query():
    ingredients = Ingredient.query.all()
    ingredientlist = []
    for i in ingredients:
        ingredientlist.append((i.id, i.name))
    return ingredientlist

class IngredientToDrinkForm(FlaskForm):
    name = SelectField("Ainesosa:", coerce=int, choices=ingredient_query())
    amount = StringField("Määrä", [validators.InputRequired()])
    submit = SubmitField("Lisää ainesosa drinkkiin")

    class Meta:
        csrf=False

class IngredientForm(FlaskForm):

    name = StringField("Nimi", [validators.InputRequired()])
    submit = SubmitField("Lisää ainesosa")

    class Meta:
        csrf=False


