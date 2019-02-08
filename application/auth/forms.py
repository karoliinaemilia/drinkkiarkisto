from flask_wtf import FlaskForm
from wtforms import PasswordField, StringField, validators
  
class LoginForm(FlaskForm):
    username = StringField("Käyttäjätunnus")
    password = PasswordField("Salasana")
  
    class Meta:
        csrf = False

class SignupForm(FlaskForm):
    name = StringField("Nimi", [validators.input_required(), validators.length(3, 20, message='Nimen on oltava vähintään 3 ja korkeintaan 20 merkkiä pitkä')])
    username = StringField("Käyttäjätunnus", [validators.InputRequired(), validators.length(3, 20, message='Käyttäjätunnuksen on oltava vähintään 3 ja korkeintaan 20 merkkiä pitkä')])
    password = PasswordField("Salasana",  [validators.InputRequired(), validators.EqualTo('confirmation', message='Salasanojen tulee olla samat')])
    confirmation = PasswordField("Kirjoita salasana uudestaan")

    class Meta:
        csrf = False