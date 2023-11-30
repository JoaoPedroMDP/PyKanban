#  coding: utf-8


import datetime
from typing import List

from classes.database_handler import DatabaseHandler
from classes.pure.task import Task


class Column(DatabaseHandler):
    FILE_NAME = "db_columns.json"
    COLUMNS = []

    def __init__(self, id: int, name: str, tasks: List[Task], table_id: int, position: int):
        self.id = id
        self.name = name
        self.tasks = tasks
        self.position = position
        self.table_id = table_id

    def __str__(self):
        return (f"Column(id={self.id}, name={self.name}, "
                f"tasks={self.tasks}, table_id={self.table_id}, "
                f"position={self.position})")

    @classmethod
    def to_db(cls):
        return {"columns": [x.to_db_dict() for x in cls.COLUMNS]}

    @classmethod
    def from_db(cls, data: dict):
        cls.COLUMNS = [cls.from_db_dict(x) for x in data["columns"]]

    @classmethod
    def from_dict(cls, data: dict):
        return cls(
            id=data["id"],
            name=data["name"],
            tasks=Task.get_tasks_from_column_id(data["id"]),
            table_id=data["table_id"],
            position=data["position"]
        )

    def to_dict(self):
        return {
            "id": self.id,
            "name": self.name,
            "table_id": self.table_id,
            "position": self.position
        }

    @classmethod
    def from_db_dict(cls, data: dict):
        return cls(
            id=data["id"],
            name=data["name"],
            tasks=Task.get_tasks_from_column_id(data["id"]),
            table_id=data["table_id"],
            position=data["position"]
        )

    def to_db_dict(self):
        return {
            "id": self.id,
            "name": self.name,
            "table_id": self.table_id,
            "position": self.position
        }

    def delete(self):
        Column.COLUMNS = [x for x in Column.COLUMNS if x.id != self.id]
        self.save_memory()

    def add_task(self, task: Task):
        self.tasks.append(task)
        task.move(self.id)

    def get_stale_tasks(self, days) -> List[Task]:
        # Retorna todas as tasks que já estão numa mesma coluna há mais de 'days' dias
        now = datetime.datetime.now()
        stale_tasks = []
        for task in self.tasks:
            task_moved_datetime = datetime.datetime.fromtimestamp(task.moved)
            if (now - task_moved_datetime).days >= days:
                stale_tasks.append(task)

        return stale_tasks

    def remove_task(self, task: Task):
        self.tasks.remove(task)

    def get_idle_task_count(self) -> int:
        count = 0
        for task in self.tasks:
            if task.is_idle():
                count += 1

        return count

    @classmethod
    def get_columns_from_table_id(cls, table_id: int) -> List['Column']:
        return list(filter(lambda column: column.table_id == table_id, cls.COLUMNS))

    @classmethod
    def create(cls, name: str, table_id: int, position: int) -> 'Column':
        column = {
            "id": cls.biggest_id(cls.COLUMNS) + 1,
            "name": name,
            "tasks": [],
            "table_id": table_id,
            "position": position
        }
        column = Column.from_dict(column)
        cls.COLUMNS.append(column)
        column.save_memory()

        return column
