#  coding: utf-8

USERS = [
    {
        "id": 0,
        "name": "joao",
        "login": "",
        "password": ""
    }
]


TABLES = [
    {
        "id": 0,
        "name": "Escola",
        "user_id": 0,
    }
]


COLUMNS = [
    {
        "id": 0,
        "name": "A fazer",
        "table_id": 0
    },
    {
        "id": 1,
        "name": "Fazendo",
        "table_id": 0
    },
    {
        "id": 2,
        "name": "Feito",
        "table_id": 0
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
