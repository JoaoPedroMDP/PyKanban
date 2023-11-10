import datetime
from typing import List

from classes.pure.Task import Task
from memory import get_tasks_from_column_id


class Column:
    def __init__(self, id: int, name: str, tasks: List[Task], table_id: int):
        self.id = id
        self.name = name
        self.tasks = tasks
        self.table_id = table_id

    def __str__(self):
        return f"Column(id={self.id}, name={self.name}, tasks={self.tasks}, table_id={self.table_id})"

    @classmethod
    def from_dict(cls, data: dict):
        return cls(
            id=data["id"],
            name=data["name"],
            tasks=[Task.from_dict(x) for x in get_tasks_from_column_id(data["id"])],
            table_id=data["table_id"]
        )

    def add_task(self, task: Task):
        self.tasks.append(task)
        task.move(self)

    def send_task(self, task: Task, column: 'Column') -> None:
        self.tasks.remove(task)
        column.add_task(task)

    def get_stale_tasks(self, days) -> List[Task]:
        # Retorna todas as tasks que já estão numa mesma coluna há mais de 'days' dias
        now = datetime.datetime.now()
        stale_tasks = []
        for task in self.tasks:
            task_moved_datetime = datetime.datetime.fromtimestamp(task.moved)
            if (now - task_moved_datetime).days >= days:
                stale_tasks.append(task)

        return stale_tasks
