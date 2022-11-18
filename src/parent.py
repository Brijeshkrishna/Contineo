from flask import Blueprint, render_template

parent = Blueprint("parent", __name__, template_folder="template", static_folder="static")


@parent.route("/")
def home():
    return  render_template("/parent/home.html")