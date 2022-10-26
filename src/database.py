from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi
from bson.objectid import ObjectId
from flask_bcrypt import Bcrypt
from typing import Optional


client = MongoClient(
    "mongodb+srv://brijesh:sPVBlaQf9ZT93xHr@cluster0.cvljjpg.mongodb.net/?retryWrites=true&w=majority",
    server_api=ServerApi("1"),
)
db = client.Database.ContineoUser
bcrypt= Bcrypt()

def check_password(email,password) -> Optional[ObjectId]:
    print((email,password))
    res = db.find_one({"email": email})
    if res != None:
        if  bcrypt.check_password_hash(res['password_hash'],password):
            return res['_id']
    return None