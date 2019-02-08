from flask_wtf import FlaskForm
from wtforms import StringField, validators

class DrinkForm(FlaskForm):
    name = StringField("Nimi:", [validators.InputRequired(), validators.length(3, 20, message='Nimen on oltava vähintään 3 ja korkeintaan 20 merkkiä pitkä')])
    drinktype = StringField("Juomalaji:", [validators.InputRequired(), validators.length(3, 20, message='Juomalajin on oltava vähintään 3 ja korkeintaan 20 merkkiä pitkä')])
 
    class Meta:
        csrf = False