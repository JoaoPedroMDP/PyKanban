#  coding: utf-8
from threading import Thread
from time import sleep
from typing import List

from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QMainWindow, QHBoxLayout, QVBoxLayout
from PyQt5.uic import loadUi

from classes.pure.Column import Column
from classes.pure.Table import Table
from classes.pure.Task import Task
from memory import get_tables_from_user_id
from qt_uis.screens import HasStatusBar
from qt_uis.widgets.column_widget import ColumnWidget
from qt_uis.widgets.table_list_item_widget import TableListItemWidget
from qt_uis.widgets.task_widget import TaskWidget


class TableScreen(QMainWindow, HasStatusBar):
    def __init__(self, navigator, data: dict):
        super(TableScreen, self).__init__()
        loadUi("qt_uis/screens/raw_screens/TableScreen.ui", self)
        self.navigator = navigator
        self.create_task_button.released.connect(self.create_task)
        self.data = data
        self.tables: List[Table] = self.get_tables()
        self.opened_table: Table = self.tables[0]
        self.table_name.setText(self.opened_table.name)
        self.table_layout: QHBoxLayout = QHBoxLayout(self.table)
        self.populate_table_list()
        self.create_table_button.released.connect(lambda: self.navigator.navigate("new_table"))
        self.update_table()
        # Adiciona uma thread que atualiza o numero de tasks pendentes a cada 5 segundos
        thread = Thread(target=self.update_idle_tasks_counter)
        thread.start()

    def populate_table_list(self):
        vertical_layout = QVBoxLayout(self.table_list)
        vertical_layout.setSpacing(2)
        vertical_layout.setContentsMargins(0, 2, 0, 2)
        vertical_layout.setAlignment(Qt.AlignTop)

        for table in self.tables:
            table_item = TableListItemWidget(table)
            table_item.set_table.connect(self.change_table)
            vertical_layout.addWidget(table_item)

    def change_table(self, table: Table):
        self.opened_table = table
        self.table_name.setText(table.name)
        self.update_table()

    def update_idle_tasks_counter(self):
        while True:
            idle_tasks_count = self.opened_table.get_idle_task_count()
            self.statusBar().showMessage(str(idle_tasks_count))
            sleep(1)

    def get_tables(self) -> List[Table]:
        tables = get_tables_from_user_id(self.navigator.user["id"])
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
            new_column = self.create_column_widget(column)
            self.table_layout.addWidget(new_column)
            # self.table.setMinimumWidth(self.table.width() + new_column.width())

        self.table.update()

    def clear_table(self):
        while not self.table_layout.isEmpty():
            to_delete = self.table_layout.takeAt(0)
            if to_delete is not None:
                widget = to_delete.widget()
                widget.deleteLater()

    def create_column_widget(self, column: Column):
        new_column: ColumnWidget = ColumnWidget(column, self.table)

        for task in column.tasks:
            print("Adicionando task" + task.name)
            new_item = TaskWidget(task, new_column)
            new_item.move_task.connect(self.move_task)
            new_column.add_task(new_item)

        return new_column

    def move_task(self, task: Task, direction: int):
        self.opened_table.move_task(task, direction)
        self.update_table()
