#  coding: utf-8
from PyQt5.QtWidgets import QMainWindow, QListWidget, QListWidgetItem
from PyQt5.uic import loadUi

from classes.Column import Column
from classes.Table import Table
from classes.Task import Task
from memory import TABLES
from screens.raw_screens.TableScreen import Ui_TableScreen


class TableScreen(QMainWindow, Ui_TableScreen):
    def __init__(self, navigator, data: dict):
        super(TableScreen, self).__init__()
        loadUi("screens/raw_screens/TableScreen.ui", self)
        self.navigator = navigator
        self.create_task_button.released.connect(self.create_task)
        self.data = data
        self.tables = self.get_tables()
        self.opened_table = self.tables[0]
        self.table_name.setText(self.opened_table.name)
        self.update_table()

    def get_tables(self):
        tables = list(filter(lambda item: item["user_id"] == self.data["user"]["id"], TABLES))
        return [Table.from_dict(data) for data in tables]

    def create_task(self):
        task_title = self.create_task_text_input.text()
        table_first_column: Column = self.opened_table.columns[0]
        task: Task = Task(task_title, table_first_column.id)
        table_first_column.add_task(task)
        self.update_table()

    def update_table(self):
        print(self.opened_table)
        for column in self.opened_table.columns:
            new_column = QListWidget(self.table)
            for task in column.tasks:
                new_item = QListWidgetItem(task.name, new_column)
                new_column.addItem(new_item)

        self.table.update()
