# /auth
from flask import Blueprint, render_template, Response,session,redirect,url_for,flash
from flask_login import login_user,logout_user,current_user
from ..form.form import LoginForm
from ..database.database import check_password


auth = Blueprint("auth", __name__, template_folder="template", static_folder="static")


@auth.route('/logout',methods=['GET'])
def logout():
    session.clear()
    logout_user()
    return redirect(url_for('auth.login'))




@auth.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated :
        return redirect(url_for('admin.home'))
    
    form = LoginForm()
    if form.validate_on_submit():
        res =check_password(form.email.data,form.password.data)
        if res != None:
            login_user(res,remember=form.remember.data)
            return redirect(url_for('admin.home'))
        else:
            flash('Login Unsuccessful. Please check username and password', 'danger')
            
    return  render_template('auth/login.html', form=form,title="Login")