from typing import Optional
from asgiref.wsgi import WsgiToAsgi
from flask import Flask, redirect, url_for, request, Response
from flask_bcrypt import Bcrypt
from flask_login import LoginManager, current_user
from src.database import get_by_id
from src.admin import admin
from src.auth import auth
from src.student import student
from src.parent import parent
from src.teacher import teacher


from src.error import error
from src.model import give_user_home

app = Flask(__name__, template_folder="template", static_folder="static")
app.secret_key = 'super secret key'
bcrypt = Bcrypt()

login_manager = LoginManager(app)
login_manager.login_view = 'login'
login_manager.login_message_category = 'info'
login_manager.session_protection = "strong"

app.register_blueprint(auth, url_prefix="/auth")

app.register_blueprint(admin, url_prefix="/admin")
app.register_blueprint(teacher, url_prefix="/teacher")
app.register_blueprint(student, url_prefix="/student")
app.register_blueprint(parent, url_prefix="/parent")

app.register_blueprint(error)


@login_manager.user_loader
def load_user(user_id):
    return get_by_id(user_id)


@app.route("/")
async def home():
    return redirect(url_for("auth.login"))


@app.route("/logout")
async def logout():
    return redirect(url_for("auth.logout"))



@app.before_request
async def before_request() -> Optional[Response]:

    # if user is logined
    if current_user.is_authenticated :
       
        if request.endpoint not in ["auth.login", "static","auth.logout","logout"]:

            user =load_user(current_user.get_id())

            try:
                endpoint = request.endpoint.split('.')[0]
            except:
                return redirect(give_user_home(user))

            # check the priority_level and endpoint
            if user.endpoint != endpoint:
                return redirect(give_user_home(user))


    # if the user in not login or static domain redirect to login
    elif request.endpoint not in ["auth.login", "static"]:
            return redirect(url_for('auth.login'))



app = WsgiToAsgi(app)