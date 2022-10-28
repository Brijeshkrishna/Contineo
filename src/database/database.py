from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi
from bson.objectid import ObjectId
from flask_bcrypt import Bcrypt
from typing import Optional
from ..model.model import User


client:MongoClient = MongoClient(
    "mongodb+srv://brijesh:sPVBlaQf9ZT93xHr@cluster0.cvljjpg.mongodb.net/?retryWrites=true&w=majority",
    server_api=ServerApi("1"),
)
db = client.Database.ContineoUser
bcrypt= Bcrypt()

def check_password(email,password) -> Optional[User]:
    res = db.find_one({"email": email})
    if res != None:
        if  bcrypt.check_password_hash(res['password_hash'],password):
            print("chck")
            return User(id=res['_id'],email=res['email'],username=res['username'],priority_level=res['priority_level'])
    return None

def get_by_id(user_id) -> Optional[User]:
    res = db.find_one({"_id": ObjectId(user_id)})
    if res != None:
            return User(id=res['_id'],email=res['email'],username=res['username'],priority_level=res['priority_level'])
    return None