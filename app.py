from flask import Flask,redirect,url_for,request,Response
from flask_bcrypt import Bcrypt
from flask_login import LoginManager,current_user
from src.database.database import get_by_id
from src.admin.admin import admin
from src.auth.auth import auth
from src.error.error import error

app = Flask(__name__, template_folder="template", static_folder="static")
app.secret_key = 'super secret key'
bcrypt= Bcrypt()

login_manager = LoginManager(app)
login_manager.login_view = 'login'
login_manager.login_message_category = 'info'
login_manager.session_protection = "strong"


app.register_blueprint(admin,url_prefix="/admin")
app.register_blueprint(auth,url_prefix="/auth")
app.register_blueprint(error)


@login_manager.user_loader
def load_user(user_id):
    return get_by_id(user_id)


@app.before_request
def before_request() -> Response:
    if request.endpoint not in ["auth.login","static"] and not current_user.is_authenticated :
        return redirect(url_for('auth.login'))
        
@app.route("/")
def root():
    return redirect(url_for('admin.home'))