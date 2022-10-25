from flask import *
import flask_login
from flask_login import current_user

app = Flask(__name__, template_folder="template", static_folder="static")


login_manager = flask_login.LoginManager()
login_manager.init_app(app)
login_manager.session_protection = "strong"


app.secret_key = 'super secret key'


users = {'foo@bar.tld': {'password': 'secret'}}

class User(flask_login.UserMixin):
    pass


@login_manager.user_loader
def user_loader(username):
    if username not in users:
        return
    user = User()
    user.id = username
    return user


@login_manager.request_loader
def request_loader(request):
    username = request.form.get('username')
    if username not in users:
        return
    user = User()
    user.id = username
    return user

@app.route('/login', methods=['GET', 'POST'])
@app.route('/', methods=['GET', 'POST'])
def login():

    if request.method == 'GET':
        if current_user.is_authenticated :
            return redirect(url_for('home'))
        return render_template("login.html")

    username = request.form['username']
    if username in users and request.form['password'] == users[username]['password']:
        user = User()
        user.id = username
        flask_login.login_user(user)
        return redirect(url_for('home'))
    return render_template("login.html")


@app.route('/dashboard')
@flask_login.login_required
def home():
    return render_template("home.html")


@app.route('/logout')
def logout():
    session.clear()
    flask_login.logout_user()
    return redirect(url_for('login'))



@login_manager.unauthorized_handler
def unauthorized_handler():
    return redirect(url_for('login'))