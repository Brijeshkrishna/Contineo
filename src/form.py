from flask_wtf import FlaskForm
from wtforms import StringField,PasswordField,SubmitField,BooleanField
from wtforms.validators import *

class LoginForm(FlaskForm):
    email = StringField('Email',validators=[DataRequired(), Email()])
    password=  PasswordField("Password",validators=[DataRequired()])
    remember = BooleanField('Remember Me')
    submit = SubmitField("Login")