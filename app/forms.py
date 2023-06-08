from flask_wtf import FlaskForm
from wtforms import SubmitField, StringField, PasswordField
from wtforms.validators import DataRequired, Email

class RegisterForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    submit = SubmitField('Register')


class LoginForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    submit = SubmitField('Login')


class CollectionForm(FlaskForm):
    name = StringField("Superhero Name", validators=[DataRequired()])
    description = StringField('Superhero Description')
    comics = StringField('This Hero appeared in how many comics?')
    superpower = StringField('Superpowers')
    submit = SubmitField('Submit')