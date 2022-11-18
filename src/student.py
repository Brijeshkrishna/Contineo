from flask import Blueprint, render_template

student = Blueprint("student", __name__, template_folder="template", static_folder="static")


@student.route("/")
def home():
    return  render_template("/student/home.html")