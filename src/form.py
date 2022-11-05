from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField
from wtforms.validators import DataRequired, Regexp


class LoginForm(FlaskForm):
    email_username = StringField("Email or Username", validators=[DataRequired(), Regexp(
        "[ ]*^(1[sS][iI][0-9][0-9][A-z][A-z][0-9][0-9][0-9]|admin)[ ]*$")])
    password = PasswordField("Password", validators=[DataRequired()])
    remember = BooleanField("Remember Me")
    submit = SubmitField("Login")
