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
