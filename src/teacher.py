from flask import Blueprint, render_template

teacher = Blueprint("teacher", __name__, template_folder="template", static_folder="static")


@teacher.route("/")
def home():
    return  render_template("/teacher/home.html")