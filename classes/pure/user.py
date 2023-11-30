#  coding: utf-8
from typing import Optional

from classes.database_handler import DatabaseHandler
from exceptions import ExpectedException


class User(DatabaseHandler):
    FILE_NAME = "db_users.json"
    USERS = []

    def __init__(self, id: int, name: str, password: str, login: str):
        self.id = id
        self.name = name
        self.password = password
        self.login = login

    def __str__(self):
        return f"User(id={self.id}, name={self.name}, password={self.password}, login={self.login})"

    @classmethod
    def to_db(cls):
        return {"users": [x.to_db_dict() for x in cls.USERS]}

    @classmethod
    def from_db(cls, data: dict):
        cls.USERS = [cls.from_db_dict(x) for x in data["users"]]

    @staticmethod
    def from_dict(data: dict) -> 'User':
        return User(
            id=data["id"],
            name=data["name"],
            password=data["password"],
            login=data["login"]
        )

    def to_dict(self) -> dict:
        return {
            "id": self.id,
            "name": self.name,
            "password": self.password,
            "login": self.login
        }

    def delete(self):
        User.USERS = [x for x in User.USERS if x.id != self.id]
        self.save_memory()

    @classmethod
    def from_db_dict(cls, data: dict):
        return cls.from_dict(data)

    def to_db_dict(self):
        return self.to_dict()

    @classmethod
    def get_user_by_login(cls, login: str) -> Optional['User']:
        results = list(filter(lambda user: user.login == login, cls.USERS))
        if results and len(results) > 0:
            return results[0]

        return None

    @classmethod
    def create(cls, name: str, login: str, password: str):
        # Verifico se já tem um usuário com o mesmo login
        if cls.get_user_by_login(login):
            raise ExpectedException("Já existe um usuário com esse login")

        user = {
            "id": len(cls.USERS),
            "name": name,
            "login": login,
            "password": password
        }
        user = cls.from_dict(user)
        cls.USERS.append(user)
        user.save_memory()

        return user
