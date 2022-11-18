from flask import url_for
from flask_login import UserMixin
from bson import ObjectId

class User(UserMixin):
    def __init__(
        self, id: ObjectId, email: str, username: str, priority_level: int
    ) -> None:
        self.id: ObjectId = id
        self.email: str = email
        self.username: str = username
        self.priority_level: int = priority_level
        if priority_level == 0:
            self.endpoint = 'admin'
        elif priority_level == 1:
            self.endpoint = 'teacher'
        elif priority_level == 2:
            self.endpoint = 'student'
        elif priority_level == 3:
            self.endpoint = 'parent'


def give_user_home(user:User):
    return url_for(user.endpoint + ".home")
