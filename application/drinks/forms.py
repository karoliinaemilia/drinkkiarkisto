from flask_wtf import FlaskForm
from wtforms import StringField, validators, SelectField, SubmitField, TextAreaField
from application.drinktypes.models import Drinktype

def drinktype_query():
    return [(dt.id, dt.name) for dt in Drinktype.query.all()]

class DrinkForm(FlaskForm):
    name = StringField("Nimi:", [validators.InputRequired(), validators.length(3, 20, message='Nimen on oltava vähintään 3 ja korkeintaan 20 merkkiä pitkä')])
    drinktype = SelectField(u"Juomalaji:", coerce=int, choices=drinktype_query())
    instructions = TextAreaField("Ohjeet: ", [validators.InputRequired(), validators.length(10, 280, message='Ohjeen on oltava vähintään 10 ja korkeintaan 280 merkkiä pitkä')])
    submit = SubmitField("Lisää drinkki")

    class Meta:
        csrf = False

class SearchForm(FlaskForm):
    keyword = StringField("Hakusana: ", [validators.InputRequired()])
    submit = SubmitField("Hae")

    class Meta:
        csrf = False