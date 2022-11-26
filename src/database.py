
from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi
from bson.objectid import ObjectId
from flask_bcrypt import Bcrypt
from typing import Optional
from src.model import User
from datetime import date

client: MongoClient = MongoClient(
    "mongodb+srv://brijesh:sPVBlaQf9ZT93xHr@cluster0.cvljjpg.mongodb.net/?retryWrites=true&w=majority",
    server_api=ServerApi("1"),
)
db: client.Database.ContineoUser = client.Database.ContineoUser
bcrypt: Bcrypt = Bcrypt()


def check_password(email: str, password: str) -> Optional[User]:
    res = db.find_one({"email": email})
    if res != None:
        if bcrypt.check_password_hash(res['password_hash'], password):
            return User(id=res['_id'], email=res['email'], username=res['username'],
                        priority_level=res['priority_level'])
    return None


def get_by_id(user_id) -> Optional[User]:
    res = db.find_one({"_id": ObjectId(user_id)})
    if res != None:
        return User(id=res['_id'], email=res['email'], username=res['username'], priority_level=res['priority_level'])
    return None


def add_user(name: str, usn: str, dob: date, password: str, sem):
    if not check_student_exists(usn):
        print(dob.strftime("%d-%m-%y"))
        db.insert_one({"username": name, "usn": usn, "email": usn + "@sit.ac.in", "priority_level": 2,
                       "password_hash": bcrypt.generate_password_hash(password).decode("utf-8"),
                       "dob": dob.strftime("%Y-%m-%d"), "sem": sem})
        return "Success", 'success'
    return "USN exists", 'danger'


def update_user(old: str, name: str, usn: str, dob: date, password: str, sem):

    if (old != usn and check_student_exists(usn)) or not check_student_exists(old):
        return "USN exists check again", 'danger'
    db.update_many({"usn": old},
                   {"$set": {"username": name, "usn": usn, "email": usn + "@sit.ac.in", "priority_level": 2,
                             "password_hash": bcrypt.generate_password_hash(password).decode("utf-8"),
                             "dob": dob.strftime("%Y-%m-%d"), "sem": sem}}
                   )
    return "Success", 'success'


def add_teach(name: str, cname: str, dob: date, password: str, sem):
    if not check_teach_exists(cname):
        print(dob.strftime("%d-%m-%y"))
        db.insert_one({"username": name, "cname": cname, "email": cname + "@sit.ac.in", "priority_level": 1,
                       "password_hash": bcrypt.generate_password_hash(password).decode("utf-8"),
                       "dob": dob.strftime("%Y-%m-%d"), "sem": sem})
        return "Success", 'success'
    return "USN exists", 'danger'


def update_teach(old_cname: str, name: str, cname: str, dob: date, password: str, sem):

    if (old_cname != cname and check_teach_exists(cname)) or not check_teach_exists(old_cname):
        return "cname exists check again", 'danger'
    db.update_many({"cname": old_cname},
                   {"$set": {"username": name, "cname": cname, "email": cname + "@sit.ac.in", "priority_level": 1,
                             "password_hash": bcrypt.generate_password_hash(password).decode("utf-8"),
                             "dob": dob.strftime("%Y-%m-%d"), "sem": sem}}
                   )
    return "Success", 'success'


def delete_teach(cname):
    db.delete_one({"cname": cname})


def check_teach_exists(cname: str):
    if get_teach_by_cname(cname) is None:
        return 0
    return 1


def get_teach_by_cname(cname: str):
    return db.find_one({"cname": cname})


def delete_user(usn):
    db.delete_one({"usn": usn})


def get_all_student():
    return db.find({"priority_level": 2})


def get_all_teachers():
    return db.find({"priority_level": 1})


def get_student_by_usn(usn: str):
    return db.find_one({"usn": usn})


def check_student_exists(usn: str):
    if get_student_by_usn(usn) is None:
        return 0
    return 1
