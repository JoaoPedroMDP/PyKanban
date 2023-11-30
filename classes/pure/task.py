#  coding: utf-8
import datetime
from typing import List

from classes.database_handler import DatabaseHandler
from config import IDLE_SECONDS_THRESHOLD, DATETIME_FORMAT


class Task(DatabaseHandler):
    TASKS = []
    FILE_NAME = "db_tasks.json"

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
            "created": self.created.strftime(DATETIME_FORMAT),
            "updated": self.updated.strftime(DATETIME_FORMAT),
            "moved": self.moved.strftime(DATETIME_FORMAT)
        }

    @classmethod
    def from_dict(cls, data: dict):
        if "created" in data and type(data["created"]) is str:
            data["created"] = datetime.datetime.strptime(data["created"], DATETIME_FORMAT)

        if "updated" in data and type(data["updated"]) is str:
            data["updated"] = datetime.datetime.strptime(data["updated"], DATETIME_FORMAT)

        if "moved" in data and type(data["moved"]) is str:
            data["moved"] = datetime.datetime.strptime(data["moved"], DATETIME_FORMAT)

        return cls(
            id=data["id"],
            name=data["name"],
            column_id=data["column_id"],
            created=data["created"] if "created" in data else datetime.datetime.now(),
            updated=data["updated"] if "updated" in data else datetime.datetime.now(),
            moved=data["moved"] if "moved" in data else datetime.datetime.now()
        )

    @classmethod
    def from_db_dict(cls, data: dict):
        return cls.from_dict(data)

    def to_db_dict(self):
        return self.to_dict()

    @classmethod
    def to_db(cls):
        return {"tasks": [x.to_db_dict() for x in cls.TASKS]}

    @classmethod
    def from_db(cls, data: dict):
        cls.TASKS = [cls.from_db_dict(x) for x in data["tasks"]]

    def delete(self):
        Task.TASKS = [x for x in Task.TASKS if x.id != self.id]
        self.save_memory()

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

    def is_idle(self):
        now = datetime.datetime.now()
        moved_datetime = datetime.datetime.fromtimestamp(self.moved.timestamp())
        return (now - moved_datetime).seconds >= IDLE_SECONDS_THRESHOLD

    @classmethod
    def create(cls, name: str, column_id: int):
        task = {
            "id": cls.biggest_id(cls.TASKS) + 1,
            "name": name,
            "column_id": column_id
        }
        task = Task.from_dict(task)
        cls.TASKS.append(task)
        task.save_memory()

        return task

    def update(self):
        self_on_memory = [x for x in self.TASKS if x.id == self.id][0]
        self_on_memory.column_id = self.column_id
        self_on_memory.name = self.name
        self_on_memory.moved = self.moved
        self_on_memory.updated = self.updated
        self_on_memory.created = self.created

    @classmethod
    def get_tasks_from_column_id(cls, column_id: int) -> List['Task']:
        return list(filter(lambda item: item.column_id == column_id, cls.TASKS))
