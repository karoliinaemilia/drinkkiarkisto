from flask_wtf import FlaskForm
from wtforms import StringField, validators, SelectField, SubmitField, ValidationError
from application.ingredients.models import Ingredient

def ingredient_query():
    return [(i.id, i.name) for i in Ingredient.query.all()]

class IngredientToDrinkForm(FlaskForm):
    name = SelectField(u"Ainesosa:", coerce=int, choices=ingredient_query())
    amount = StringField("Määrä", [validators.InputRequired()])
    submit = SubmitField("Lisää ainesosa drinkkiin")

    class Meta:
        csrf=False

class IngredientForm(FlaskForm):

    name = StringField("Nimi", [validators.InputRequired()])
    submit = SubmitField("Lisää ainesosa")

    class Meta:
        csrf=False


