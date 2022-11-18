# /auth
from flask import Blueprint, render_template, session, redirect, url_for, flash
from flask_login import login_user, logout_user, current_user
from src.form import LoginForm
from src.database import check_password
from .model import give_user_home


auth = Blueprint("auth", __name__, template_folder="template", static_folder="static")

@auth.route('/logout')
def logout():
    session.clear()
    logout_user()
    print("log authed")
    return  redirect(url_for('auth.login'))

    
    
@auth.route('/login', methods=['GET', 'POST'])
async def login():
    
    if current_user.is_authenticated:
        print("authed")
        return redirect(url_for('admin.home'))
    
    form = LoginForm()
    if form.validate_on_submit(): # is form is valid

        email_username=form.email_username.data

        # if @sit.ac.in not in email it append it
        if form.email_username.data.find("@sit.ac.in") == -1:
            email_username = form.email_username.data + "@sit.ac.in"
        
        #check the password
        res = check_password(email_username, form.password.data)
        
        # if password is right
        if res != None:
            #login the user
            login_user(res, remember=form.remember.data,force=True)

            # send to proper website
            return redirect(give_user_home(res))
            
        else:
            flash('Login Unsuccessful. Please check username or password', 'danger')

    return render_template("auth/login.html", form=form, title="Login")