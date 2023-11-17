#  coding: utf-8
from PyQt5.QtCore import pyqtSignal, Qt
from PyQt5.QtWidgets import QWidget, QScrollArea
from PyQt5.uic import loadUi

from classes.pure.Table import Table
from qt_uis.widgets.raw_widgets.TableListItemWidget import Ui_TableListItemWidget


class TableListItemWidget(QWidget, Ui_TableListItemWidget):
    set_table = pyqtSignal(Table)

    def __init__(self, table: Table, parent=None):
        super(TableListItemWidget, self).__init__(parent)
        loadUi("qt_uis/widgets/raw_widgets/TableListItemWidget.ui", self)
        self.table = table
        self.config_ui()
        self.table_name.setText(self.table.name)

    def mouseReleaseEvent(self, a0):
        self.set_table.emit(self.table)

    def config_ui(self):
        pass