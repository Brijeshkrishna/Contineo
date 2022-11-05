from urllib.parse import urlparse
from flask import Flask, redirect, url_for, request, Response
from flask_bcrypt import Bcrypt
from flask_login import LoginManager, current_user
from src.database import get_by_id
from src.admin import admin
from src.auth import auth
from src.error import error

app = Flask(__name__, template_folder="template", static_folder="static")
app.secret_key = 'super secret key'
bcrypt = Bcrypt()

login_manager = LoginManager(app)
login_manager.login_view = 'login'
login_manager.login_message_category = 'info'
login_manager.session_protection = "strong"

app.register_blueprint(admin, subdomain="admin")
app.register_blueprint(auth, subdomain="auth")
app.register_blueprint(error)


@login_manager.user_loader
def load_user(user_id):
    return get_by_id(user_id)


@app.route("/")
def home():
    return redirect(url_for("admin.home"))


@app.before_request
def before_request():
    current_url = urlparse(request.url)
    subdomain = current_url.netloc.split(".")[0]

    if not current_user.is_authenticated:
        if subdomain in ["admin"] and request.endpoint != "static":
            return redirect(url_for("auth.login"))


