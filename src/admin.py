# admin.localhost

from flask import Blueprint, render_template
from flask_login import login_required

admin = Blueprint("admin", __name__, template_folder="template", static_folder="static")

@login_required
@admin.route("/")
@admin.route("/dashboard")
def home() -> str:
    return render_template("/admin/home.html", title="Admin Dashboard")

@login_required
@admin.route("/dashboard/addUser")
def dashboard_add() -> str:
    return render_template("/admin/add.html", title="Add Student")