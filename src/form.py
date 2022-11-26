from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField, DateField
from wtforms.validators import DataRequired, Regexp
from flask_wtf.file import FileField, FileRequired, FileAllowed
import datetime


class LoginForm(FlaskForm):
    email_username = StringField("Email or Username", validators=[DataRequired(), Regexp(
        "[ ]*^(1[sS][iI][0-9][0-9][A-z][A-z][0-9][0-9][0-9]|[A-z]+)(@sit.ac.in)?[ ]*$")])
    password = PasswordField("Password", validators=[DataRequired()])
    remember = BooleanField("Remember Me")
    submit = SubmitField("Login")


class Admin_addstudent(FlaskForm):
    name = StringField("Name", validators=[DataRequired(), Regexp(
        "^[A-z ]{2,25}$")])
    usn = StringField("USN", validators=[DataRequired(), Regexp(
        "^1[sS][iI][0-9][0-9][A-z][A-z][0-9][0-9][0-9]$")])
    dob = DateField("Date of Birth", validators=[DataRequired()])
    sem = StringField("Sem", validators=[DataRequired(), Regexp("[1-9]")])
    #pic = FileField("Photo", validators=[FileRequired(), FileAllowed(['png'], 'PNG only!')])


class Admin_updatestudent(FlaskForm):
    name = StringField("Name", validators=[DataRequired(), Regexp(
        "^[A-z ]{2,25}$")])
    usn = StringField("USN", validators=[DataRequired(), Regexp(
        "^1[sS][iI][0-9][0-9][A-z][A-z][0-9][0-9][0-9]$")])
    dob = DateField("Date of Birth", validators=[DataRequired()])
    old = StringField("old", validators=[Regexp(
        "^1[sS][iI][0-9][0-9][A-z][A-z][0-9][0-9][0-9]$")])
    sem = StringField("Sem", validators=[DataRequired(), Regexp("[1-9]")])
    #pic = FileField("Photo", validators=[FileRequired(), FileAllowed(['png'], 'PNG only!')])


class Admin_addteach(FlaskForm):
    name = StringField("Name", validators=[DataRequired(), Regexp(
        "^[A-z ]{2,25}$")])
    cname = StringField("Cname", validators=[DataRequired(), Regexp("[A-Z]+")])
    dob = DateField("Date of Birth", validators=[DataRequired()])
    sem = StringField("Sem", validators=[DataRequired(), Regexp("[1-9]")])
    #pic = FileField("Photo", validators=[FileRequired(), FileAllowed(['png'], 'PNG only!')])


class Admin_updateteach(FlaskForm):
    name = StringField("Name", validators=[DataRequired(), Regexp(
        "^[A-z ]{2,25}$")])
    cname = StringField("Cname", validators=[DataRequired(), Regexp("[A-Z]+")])
    dob = DateField("Date of Birth", validators=[DataRequired()])
    old = StringField("old", validators=[DataRequired(), Regexp("[A-Z]+")])
    sem = StringField("Sem", validators=[DataRequired(), Regexp("[1-9]")])
    #pic = FileField("Photo", validators=[FileRequired(), FileAllowed(['png'], 'PNG only!')])
