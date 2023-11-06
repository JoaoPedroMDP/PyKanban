from typing import List

from classes.Column import Column


class Table:
    def __init__(self, id: int, name: str, user_id: int, columns: List[Column]):
        self.id = id
        self.name = name
        self.columns = columns
        self.user_id = user_id

    def __str__(self):
        return f"Table(id={self.id}, name={self.name}, user_id={self.user_id}, columns={self.columns})"

    @classmethod
    def from_dict(cls, data: dict):
        return cls(
            id=data["id"],
            name=data["name"],
            user_id=data["user_id"],
            columns=[Column.from_dict(column) for column in data["columns"]]
        )

    # METHODS
    def add_column(self, column):
        self.columns.append(column)

    def remove_column(self, column):
        self.columns.remove(column)
