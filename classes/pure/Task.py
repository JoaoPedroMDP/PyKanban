#  coding: utf-8
import datetime


class Task:
    def __init__(
            self, name: str, column_id: int,
            id: int = None, created: int = None, updated: int = None,
            moved: int = None
    ):
        self.id = id
        self._name = name
        self._column_id = column_id

        self.created = created if created else datetime.datetime.now()
        self.updated = updated if updated else datetime.datetime.now()
        self.moved = moved if moved else datetime.datetime.now()

    def __str__(self):
        return f"Task(id={self.id}, name={self.name}, column_id={self.column_id}, created={self.created}, " \
               f"updated={self.updated}, moved={self.moved})"

    def __repr__(self):
        return self.__str__()

    def to_dict(self):
        return {
            "id": self.id,
            "name": self.name,
            "column_id": self.column_id,
            "created": self.created.strftime("%Y-%m-%d %H:%M:%S"),
            "updated": self.updated.strftime("%Y-%m-%d %H:%M:%S"),
            "moved": self.moved.strftime("%Y-%m-%d %H:%M:%S")
        }

    @classmethod
    def from_dict(cls, data: dict):
        return cls(
            id=data["id"],
            name=data["name"],
            column_id=data["column_id"],
            created=data["created"] if "created" in data else datetime.datetime.now(),
            updated=data["updated"] if "updated" in data else datetime.datetime.now(),
            moved=data["moved"] if "moved" in data else datetime.datetime.now()
        )

    @property
    def name(self):
        return self._name

    @property
    def column_id(self):
        return self._column_id

    @column_id.setter
    def column_id(self, value):
        self._column_id = value
        self.touch()
        self.moved = datetime.datetime.now()

    @name.setter
    def name(self, value):
        self._name = value
        self.touch()

    # METHODS
    def touch(self):
        self.updated = datetime.datetime.now()

    def move(self, destiny_column_id: int):
        self.column_id = destiny_column_id
        self.touch()
        self.moved = datetime.datetime.now()
