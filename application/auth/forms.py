from flask_wtf import FlaskForm
from wtforms import PasswordField, StringField, validators, SubmitField, ValidationError
from application.auth.models import User
  
class LoginForm(FlaskForm):
    username = StringField("Käyttäjätunnus: ")
    password = PasswordField("Salasana: ")
    submit = SubmitField("Kirjaudu")
  
    class Meta:
        csrf = False

class SignupForm(FlaskForm):
    name = StringField("Nimi", [validators.input_required(), validators.length(3, 20, message='Nimen on oltava vähintään 3 ja korkeintaan 20 merkkiä pitkä')])
    username = StringField("Käyttäjätunnus", [validators.InputRequired(), validators.length(3, 20, message='Käyttäjätunnuksen on oltava vähintään 3 ja korkeintaan 20 merkkiä pitkä')])
    password = PasswordField("Salasana",  [validators.InputRequired(), validators.EqualTo('confirmation', message='Salasanojen tulee olla samat'), validators.length(3, message='Salasanan on oltava vähintään 3 merkkiä pitkä')])
    confirmation = PasswordField("Kirjoita salasana uudestaan")
    submit = SubmitField("Luo tunnus")

    class Meta:
        csrf = False

    def validate_username(self, username):
        user = User.query.filter_by(username=username.data).first()
        if user is not None:
            raise ValidationError("Käyttäjänimi on varattu")

class PasswordForm(FlaskForm):
    password = PasswordField("Nykyinen salasana: ", [validators.InputRequired()])
    new_password = PasswordField("Uusi salasana: ", [validators.InputRequired(), validators.length(3, message='Salasanan on oltava vähintään 3 merkkiä pitkä')])
    submit = SubmitField("Vaihda salasana")
    
    class Meta:
        csrf = False