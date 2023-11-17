from typing import List

from classes.pure.Column import Column
from classes.pure.Task import Task
from consts import BACKWARD, FORWARD
from memory import get_columns_from_table_id


class Table:
    def __init__(self, id: int, name: str, user_id: int, columns: List[Column]):
        self.id = id
        self.name = name
        self.columns = columns
        self.columns.sort(key=lambda x: x.position)
        self.user_id = user_id

    def __str__(self):
        return f"Table(id={self.id}, name={self.name}, user_id={self.user_id}, columns={self.columns})"

    @classmethod
    def from_dict(cls, data: dict):
        return cls(
            id=data["id"],
            name=data["name"],
            user_id=data["user_id"],
            columns=[Column.from_dict(x) for x in get_columns_from_table_id(data["id"])]
        )

    # METHODS
    def add_column(self, column):
        self.columns.append(column)

    def remove_column(self, column):
        self.columns.remove(column)

    def get_column_by_position(self, position: int):
        """
        O index de uma coluna coincidirá com sua posição na ordem de exibição
        """
        return self.columns[position]

    def get_column_by_id(self, id: int):
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
        if next_position >= len(self.columns):
            current_column.remove_task(task)
            return

        next_column: Column = self.get_column_by_position(next_position)
        task.column_id = next_column.id
        current_column.remove_task(task)
        next_column.add_task(task)

    def move_task_forward(self, task: Task):
        self.move_task(task, FORWARD)

    def move_task_backward(self, task: Task):
        self.move_task(task, BACKWARD)

    def get_idle_task_count(self):
        count = 0
        for column in self.columns:
            count += column.get_idle_task_count()

        return count
