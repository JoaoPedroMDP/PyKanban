#  coding: utf-8
import json
from abc import abstractmethod, ABC
from typing import List, Dict


class DatabaseHandler(ABC):
    FILE_NAME = None

    @classmethod
    @abstractmethod
    def create(cls, *args, **kwargs):
        raise NotImplementedError

    @abstractmethod
    def delete(self):
        raise NotImplementedError

    @classmethod
    @abstractmethod
    def to_db(cls):
        raise NotImplementedError

    @classmethod
    @abstractmethod
    def from_db(cls, data: dict):
        raise NotImplementedError

    @classmethod
    def save_memory(cls):
        data = cls.to_db()
        print("Salvando informações em  " + cls.FILE_NAME)
        with open(cls.FILE_NAME, "w") as file:
            json.dump(data, file, indent=4)

    @classmethod
    def load_memory(cls):
        try:
            with open(cls.FILE_NAME, "r") as file:
                print("Carregando informações de " + cls.FILE_NAME)
                data = json.load(file)
                if not data:
                    print("Não existem informações em " + cls.FILE_NAME)
                    return
                cls.from_db(data)
        except FileNotFoundError:
            print("Não existem informações em " + cls.FILE_NAME)

    @staticmethod
    def biggest_id(items: List[Dict]):
        if len(items) == 0:
            return 0
        return max(items, key=lambda item: item.id).id
