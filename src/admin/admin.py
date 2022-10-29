# /admin

from flask import Blueprint, render_template, Response, url_for,redirect

admin = Blueprint("admin", __name__, template_folder="template", static_folder="static")


@admin.route("/")
def home() -> str:
    return render_template("/admin/home.html", title="Admin Dashboard")


@admin.route("/dashboard/addUser")
def dashboard_add():
    return render_template("/admin/add.html", title="Add Student")

@admin.route("/dashboard")
def dashboard():
    return redirect(url_for("admin.home"))