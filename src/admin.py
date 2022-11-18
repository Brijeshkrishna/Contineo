# admin.localhost

import json
from flask import Blueprint, redirect, render_template, flash, request, url_for
from src.form import Admin_addstudent,Admin_Student_view
from src.database import add_user,get_all_student_by_usn,get_all_student
from datetime import date

admin = Blueprint("admin", __name__, template_folder="template", static_folder="static")



@admin.route("/")
async def home() -> str:
    return render_template("/admin/home.html", title="Admin Dashboard")    






@admin.route("/student/add" ,  methods=['GET', 'POST'])
async def student() -> str:
    form = Admin_addstudent()
    if form.validate_on_submit():
            if form.dob.data < date.today():
                res,code = add_user(form.name.data, form.usn.data, form.dob.data,form.dob.data.strftime("%d-%m-%y"))
                flash(res, code)
                return render_template("/admin/student.html", title="Add Student", form=form,data={})

            flash("Invalid Date of Birth", 'danger')
    else:
        if request.method == "POST":
            flash(str(form.errors), 'danger')

    return render_template("/admin/student.html", title="Add Student", form=form,data={})


@admin.route("/student/view/")
async def student_view() -> str:
    usn = request.args.get("usn",default="")
    rv = str(get_all_student_by_usn(usn.upper())).replace("'",'"')
    
    return {} if rv is "" else json.dumps(rv)

@admin.route("/student/update" , methods=['GET'])
async def student_update() -> str:
    return render_template("/admin/student_up.html", title="Add Student",form=Admin_addstudent())


@admin.route("/teacher")
async def teacher() -> str:
    pass


