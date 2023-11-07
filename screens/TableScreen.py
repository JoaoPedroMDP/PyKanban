#  coding: utf-8
from PyQt5.QtWidgets import QMainWindow, QListWidget, QListWidgetItem, QVBoxLayout, QHBoxLayout, QLabel, QFrame
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
        self.table_layout: QHBoxLayout = QHBoxLayout(self.table)
        self.update_table()

    def get_tables(self):
        tables = list(filter(lambda item: item["user_id"] == self.data["user"]["id"], TABLES))
        return [Table.from_dict(data) for data in tables]

    def create_task(self):
        task_title = self.create_task_text_input.text()
        if task_title == "":
            return

        table_first_column: Column = self.opened_table.columns[0]
        task: Task = Task(task_title, table_first_column.id)
        table_first_column.add_task(task)
        self.update_table()

    def update_table(self):
        self.clear_table()

        for column in self.opened_table.columns:
            print("Adicionando coluna" + column.name)
            new_column = self.create_column(column)
            self.table_layout.addWidget(new_column)

        self.table.update()

    def clear_table(self):
        while not self.table_layout.isEmpty():
            to_delete = self.table_layout.takeAt(0)
            if to_delete is not None:
                widget = to_delete.widget()
                widget.deleteLater()

    def create_column(self, column: Column):
        column_frame = QFrame(self.table)
        column_layout = QVBoxLayout(column_frame)

        new_column = QListWidget(self.table)
        for task in column.tasks:
            print("Adicionando task" + task.name)
            new_item = QListWidgetItem(task.name, new_column)
            new_column.addItem(new_item)

        column_header = QLabel(column.name, new_column)
        column_layout.addWidget(column_header)
        column_layout.addWidget(new_column)
        return column_frame
