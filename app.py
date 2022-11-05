from asgiref.wsgi import WsgiToAsgi
from flask import Flask, redirect, url_for
from flask_bcrypt import Bcrypt
from flask_login import LoginManager
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

app.register_blueprint(admin, url_prefix="/admin")
app.register_blueprint(auth, url_prefix="/auth")
app.register_blueprint(error)


@login_manager.user_loader
def load_user(user_id):
    return get_by_id(user_id)


@app.route("/")
def home():
    return redirect(url_for("admin.home"))


app = WsgiToAsgi(app)
