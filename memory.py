#  coding: utf-8
import json
from typing import List


def load_memory():
    with open("database.json", "r") as file:
        global USERS, TABLES, COLUMNS, TASKS
        data = json.load(file)
        if not data:
            print("Não existem informações no banco de dados")
            return

        print("Carregando informações do banco de dados")
        USERS = data["users"]
        TABLES = data["tables"]
        COLUMNS = data["columns"]
        TASKS = data["tasks"]


def save_memory():
    with open("database.json", "w") as file:
        data = {
            "users": USERS,
            "tables": TABLES,
            "columns": COLUMNS,
            "tasks": TASKS
        }
        json.dump(data, file, indent=4)


def create_column(name: str, table_id: int, position: int):
    column = {
        "id": len(COLUMNS),
        "name": name,
        "table_id": table_id,
        "position": position
    }
    COLUMNS.append(column)
    save_memory()


def create_table(name: str, columns: List[str], user_id: int):
    table = {
        "id": len(TABLES),
        "name": name,
        "user_id": user_id
    }
    TABLES.append(table)

    for i, column_name in enumerate(columns):
        create_column(column_name, table["id"], i)

    save_memory()


def create_user(name: str, login: str, password: str):
    user = {
        "id": len(USERS),
        "name": name,
        "login": login,
        "password": password
    }
    USERS.append(user)

    save_memory()


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

]


def get_tables_from_user_id(user_id: int):
    return list(filter(lambda item: item["user_id"] == user_id, TABLES))


def get_columns_from_table_id(table_id: int):
    return list(filter(lambda item: item["table_id"] == table_id, COLUMNS))


def get_tasks_from_column_id(column_id: int):
    return list(filter(lambda item: item["column_id"] == column_id, TASKS))


def get_user_by_login(login: str):
    results = list(filter(lambda item: item["login"] == login, USERS))
    if results:
        return results[0]
    return None
