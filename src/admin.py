# admin.localhost

import json
from flask import Blueprint, redirect, render_template, flash, request, url_for
from src.form import Admin_addstudent, Admin_updatestudent, Admin_addteach, Admin_updateteach
from src.database import add_user, get_student_by_usn, update_user, delete_user, get_teach_by_cname, delete_teach, add_teach, update_teach, get_all_teachers, get_all_student
from datetime import date
from bson.objectid import ObjectId


admin = Blueprint("admin", __name__,
                  template_folder="template", static_folder="static")


@admin.route("/")
async def home() -> str:
    return render_template("/admin/home.html", title="Admin Dashboard")


@admin.route("/student/add",  methods=['GET', 'POST'])
async def student() -> str:
    form = Admin_addstudent()
    if form.validate_on_submit():
        if form.dob.data < date.today():
            res, code = add_user(form.name.data, form.usn.data, form.dob.data,
                                 form.dob.data.strftime("%d-%m-%y"), form.sem.data)
            flash(res, code)
            return render_template("/admin/student.html", title="Add Student", form=form)

        flash("Invalid Date of Birth", 'danger')
    else:
        if request.method == "POST":
            flash(form.errors, 'danger')

    return render_template("/admin/student.html", title="Add Student", form=form)


@admin.route("/student/view/")
async def student_view() -> str:
    usn = request.args.get("usn", default="")
    rv = get_student_by_usn(usn.upper())

    if (usn == "usn"):
        rv = list(get_all_student())
        for f in rv:
            del f["_id"]
            del f["password_hash"]
            del f["priority_level"]

        return {"data": rv}

    if rv != None:
        del rv["_id"]
        del rv["password_hash"]
        del rv["priority_level"]

        return rv, 200

    return {}


@admin.route("/student/delete/")
async def student_delete() -> str:
    usn = request.args.get("usn", default="")
    rv = get_student_by_usn(usn.upper())

    if rv != None:
        delete_user(usn)
        flash("User deleted", 'success')
        return render_template("/admin/student.html", title="Add Student", form=Admin_updatestudent())

    flash("USN not found", 'warning')
    return render_template("/admin/student.html", title="Add Student", form=Admin_updatestudent())


@admin.route("/student/update", methods=['GET', 'POST'])
async def student_update() -> str:

    form = Admin_updatestudent()
    if form.validate_on_submit():
        if form.dob.data < date.today():
            res, code = update_user(form.old.data, form.name.data, form.usn.data,
                                    form.dob.data, form.dob.data.strftime("%d-%m-%y"), form.sem.data)
            flash(res, code)
            return render_template("/admin/student_up.html", title="Add Student", form=form)
        flash("Invalid Date of Birth", 'danger')

    return render_template("/admin/student_up.html", title="Add Student", form=form)


#  TEACHER

@admin.route("/teacher/add",  methods=['GET', 'POST'])
async def teacher() -> str:
    form = Admin_addteach()
    if form.validate_on_submit():
        if form.dob.data < date.today():
            res, code = add_teach(form.name.data, form.cname.data, form.dob.data,
                                  form.dob.data.strftime("%d-%m-%y"), form.sem.data)
            flash(res, code)
            return render_template("/admin/teacher.html", title="Add teacher", form=form)

        flash("Invalid Date of Birth", 'danger')
    else:
        if request.method == "POST":
            flash(form.errors, 'danger')

    return render_template("/admin/teacher.html", title="Add teacher", form=form)


@admin.route("/teacher/view/")
async def teacher_view() -> str:
    cname = request.args.get("cname", default="")

    if (cname == "cname"):
        rv = list(get_all_teachers())
        for f in rv:
            del f["_id"]
            del f["password_hash"]
            del f["priority_level"]

        return {"data": rv}

    rv = get_teach_by_cname(cname.upper())

    if rv != None:
        del rv["_id"]
        del rv["password_hash"]
        del rv["priority_level"]

        return rv, 200

    return {}


@admin.route("/teacher/delete/")
async def teacher_delete() -> str:
    usn = request.args.get("cname", default="")
    rv = get_teach_by_cname(usn.upper())

    if rv != None:
        delete_teach(usn)
        flash("User deleted", 'success')
        return render_template("/admin/teacher.html", title="Add Student", form=Admin_updateteach())

    flash("USN not found", 'warning')
    return render_template("/admin/teacher.html", title="Add Student", form=Admin_updateteach())


@admin.route("/teacher/update", methods=['GET', 'POST'])
async def teacher_update() -> str:

    form = Admin_updateteach()
    if form.validate_on_submit():
        if form.dob.data < date.today():
            res, code = update_teach(form.old.data, form.name.data, form.cname.data,
                                     form.dob.data, form.dob.data.strftime("%d-%m-%y"), form.sem.data)
            flash(res, code)
            return render_template("/admin/teacher_up.html", title="Add Student", form=form)
        flash("Invalid Date of Birth", 'danger')

    return render_template("/admin/teacher_up.html", title="Add teacher", form=form)
