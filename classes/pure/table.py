#  coding: utf-8
from typing import List, Dict, Optional

from classes.database_handler import DatabaseHandler
from classes.pure.column import Column
from classes.pure.task import Task
from consts import BACKWARD, FORWARD


class Table(DatabaseHandler):
    FILE_NAME = "db_tables.json"
    TABLES = []

    def __init__(self, id: int, name: str, user_id: int, columns: List[Column]):
        self.id = id
        self.name = name
        self.columns = columns
        self.columns.sort(key=lambda x: x.position)
        self.user_id = user_id

    def __str__(self):
        return f"Table(id={self.id}, name={self.name}, user_id={self.user_id}, columns={self.columns})"

    @classmethod
    def from_db(cls, data: dict):
        cls.TABLES = [cls.from_db_dict(x) for x in data["tables"]]

    @classmethod
    def to_db(cls):
        return {"tables": [x.to_db_dict() for x in cls.TABLES]}

    def delete(self):
        Table.TABLES = [x for x in Table.TABLES if x.id != self.id]
        self.save_memory()

    @classmethod
    def from_dict(cls, data: dict):
        cols = []
        for i in range(len(data["columns"])):
            cols.append(Column.create(data["columns"][i], data["id"], i))

        return cls(
            id=data["id"],
            name=data["name"],
            user_id=data["user_id"],
            columns=cols
        )

    def to_dict(self):
        return {
            "id": self.id,
            "name": self.name,
            "user_id": self.user_id,
            "columns": [x.to_dict() for x in self.columns]
        }

    @staticmethod
    def from_db_dict(data: dict):
        return Table(
            id=data["id"],
            name=data["name"],
            user_id=data["user_id"],
            columns=Column.get_columns_from_table_id(data["id"])
        )

    def to_db_dict(self):
        return {
            "id": self.id,
            "name": self.name,
            "user_id": self.user_id
        }

    # METHODS
    def add_column(self, column):
        self.columns.append(column)

    def remove_column(self, column):
        self.columns.remove(column)

    def get_column_by_position(self, position: int) -> Column:
        """
        O index de uma coluna coincidirá com sua posição na ordem de exibição
        """
        return self.columns[position]

    def get_column_by_id(self, id: int) -> Optional[Column]:
        for column in self.columns:
            if column.id == id:
                return column

        return None

    def move_task(self, task: Task, direction: int):
        """
        Avança a Task passada para a próxima coluna.
        Se a Task estiver na última coluna, destrói
        """
        current_column_id = task.column_id
        current_column: Column = self.get_column_by_id(current_column_id)
        next_position = current_column.position + direction
        if next_position >= len(self.columns) or next_position < 0:
            current_column.remove_task(task)
            task.delete()
            return

        next_column: Column = self.get_column_by_position(next_position)
        task.column_id = next_column.id
        task.update()
        current_column.remove_task(task)
        next_column.add_task(task)

    def move_task_forward(self, task: Task):
        self.move_task(task, FORWARD)

    def move_task_backward(self, task: Task):
        self.move_task(task, BACKWARD)

    def get_idle_task_count(self) -> int:
        count = 0
        for column in self.columns:
            count += column.get_idle_task_count()

        return count

    @classmethod
    def get_tables_from_user_id(cls, user_id: int) -> Optional[List['Table']]:
        return list(filter(lambda table: table.user_id == user_id, cls.TABLES))

    @classmethod
    def create(cls, name: str, columns: List[Dict], user_id: int):
        table = {
            "id": len(cls.TABLES),
            "name": name,
            "columns": columns,
            "user_id": user_id
        }

        table = Table.from_dict(table)
        cls.TABLES.append(table)
        table.save_memory()

        return table
