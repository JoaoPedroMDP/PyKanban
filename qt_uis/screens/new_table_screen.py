#  coding: utf-8
from PyQt5.QtWidgets import QMainWindow
from PyQt5.uic import loadUi

from consts import TABLE_NAME_LIMIT
from memory import create_table
from qt_uis.screens import HasStatusBar


class NewTableScreen(QMainWindow, HasStatusBar):
    def __init__(self, navigator, parent=None):
        super().__init__(parent)
        self.navigator = navigator
        loadUi("qt_uis/screens/raw_screens/NewTableScreen.ui", self)
        self.create_table_button.released.connect(self.create_table)

    def create_table(self):
        table_name = self.table_name_input.text()
        if table_name == "":
            self.statusbar.showMessage("Nome da tabela não pode ser vazio")
            return
        elif len(table_name) > TABLE_NAME_LIMIT:
            self.statusbar.showMessage(f"Nome da tabela não pode ter mais de {TABLE_NAME_LIMIT} caracteres")
            return

        columns = self.table_columns_input.text()
        if columns == "":
            self.statusbar.showMessage("A tabela deve ter ao menos uma coluna")
            return

        columns = columns.split(",")
        create_table(table_name, columns, self.navigator.user["id"])
        self.navigator.navigate("table")
