from bson import ObjectId
from flask import *
from form import LoginForm
from flask_bcrypt import Bcrypt
from flask_login import LoginManager,UserMixin,login_user,logout_user,current_user,login_required
from database import check_password


app = Flask(__name__, template_folder="template", static_folder="static")
app.secret_key = 'super secret key'
bcrypt= Bcrypt()

login_manager = LoginManager(app)
login_manager.login_view = 'login'
login_manager.login_message_category = 'info'
login_manager.session_protection = "strong"

class User(UserMixin):
    def __init__(self,id:ObjectId) -> None:
        self.id : ObjectId = id
 

@login_manager.user_loader
def load_user(user_id):
    user =User(user_id)
    return user


@app.route('/login', methods=['GET', 'POST'])
@app.route('/', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated :
        return redirect(url_for('home'))
    
    form = LoginForm()
    if form.validate_on_submit():
        res =check_password(form.email.data,form.password.data)
        if res != None:
            user = User()
            user.id= res
            login_user(user,remember=form.remember.data)
            return redirect(url_for('home'))
        else:
            flash('Login Unsuccessful. Please check username and password', 'danger')
    return render_template('login.html', form=form)


@login_required
@app.route('/dashboard')
def home():
    if current_user.is_anonymous :
        return redirect(url_for('login'))
    return render_template("home.html")


@app.route('/logout')
def logout():
    session.clear()
    logout_user()
    return redirect(url_for('login'))
