#  coding: utf-8
import json
from typing import List


def get_users():
    return USERS


def get_tables():
    return TABLES


def get_columns():
    return COLUMNS


def create_column(name: str, table_id: int, position: int):
    column = {
        "id": len(COLUMNS),
        "name": name,
        "table_id": table_id,
        "position": position
    }
    COLUMNS.append(column)


def create_table(name: str, columns: List[str], user_id: int):
    table = {
        "id": len(TABLES),
        "name": name,
        "user_id": user_id
    }
    TABLES.append(table)

    for i, column_name in enumerate(columns):
        create_column(column_name, table["id"], i)


def create_user(name: str, login: str, password: str):
    user = {
        "id": len(USERS),
        "name": name,
        "login": login,
        "password": password
    }
    USERS.append(user)


def load_memory():
    with open("database.json", "r") as file:
        global USERS, TABLES, COLUMNS, TASKS
        data = json.load(file)
        if not data:
            return

        USERS.extend(data["users"])
        TABLES.extend(data["tables"])
        COLUMNS.extend(data["columns"])
        TASKS.extend(data["tasks"])


def save_memory():
    with open("database.json", "w") as file:
        data = {
            "users": USERS,
            "tables": TABLES,
            "columns": COLUMNS,
            "tasks": TASKS
        }
        json.dump(data, file)


USERS = [
    {
        "id": 0,
        "name": "Administrador",
        "login": "admin",
        "password": "4dmin"
    }
]


TABLES = [
    {
        "id": 0,
        "name": "Exemplo",
        "user_id": 0,
    }
]


COLUMNS = [
    {
        "id": 0,
        "name": "A fazer",
        "table_id": 0,
        "position": 0
    },
    {
        "id": 1,
        "name": "Fazendo",
        "table_id": 0,
        "position": 1
    },
    {
        "id": 2,
        "name": "Feito",
        "table_id": 0,
        "position": 2
    }
]


TASKS = [
    {
        "id": 0,
        "name": "Estudar para a prova",
        "column_id": 0,
    },
    {
        "id": 1,
        "name": "Fazer o trabalho de LPOO",
        "column_id": 0,
    },
    {
        "id": 2,
        "name": "Trabalho de Química",
        "column_id": 1,
    },
    {
        "id": 3,
        "name": "Trabalho de Física",
        "column_id": 1,
    },
    {
        "id": 4,
        "name": "Trabalho de Matemática",
        "column_id": 2,
    },
    {
        "id": 5,
        "name": "Trabalho de Português",
        "column_id": 2,
    }
]


def get_tables_from_user_id(user_id: int):
    return list(filter(lambda item: item["user_id"] == user_id, TABLES))


def get_columns_from_table_id(table_id: int):
    return list(filter(lambda item: item["table_id"] == table_id, COLUMNS))


def get_tasks_from_column_id(column_id: int):
    return list(filter(lambda item: item["column_id"] == column_id, TASKS))
