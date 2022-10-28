# /admin

from flask import Blueprint, render_template, Response

admin = Blueprint("admin", __name__, template_folder="template", static_folder="static")


@admin.route("/dashboard")
def home() -> Response:
    return render_template("/admin/home.html", title="Admin Dashboard")


@admin.route("/dashboard/addUser")
def dashboard_add():
    return render_template("/admin/add.html", title="Add Student")
