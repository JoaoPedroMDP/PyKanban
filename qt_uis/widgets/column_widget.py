#  coding: utf-8
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QWidget, QVBoxLayout, QScrollArea
from PyQt5.uic import loadUi

from classes.pure.Column import Column
from qt_uis.widgets.raw_widgets.ColumnWidget import Ui_ColumnWidget
from qt_uis.widgets.task_widget import TaskWidget


class ColumnWidget(QWidget, Ui_ColumnWidget):
    def __init__(self, column: Column, parent=None):
        super(ColumnWidget, self).__init__(parent)
        loadUi("qt_uis/widgets/raw_widgets/ColumnWidget.ui", self)
        self.list_layout = QVBoxLayout(self.tasks_scroll_area.widget())

        self.config_ui()
        self.column = column
        self.column_name_label.setText(column.name)

    def config_ui(self):
        self.list_layout.setSpacing(2)
        self.list_layout.setContentsMargins(0, 2, 0, 2)
        self.list_layout.setAlignment(Qt.AlignTop)
        self.tasks_scroll_area.setSizeAdjustPolicy(QScrollArea.AdjustToContents)

    def add_task(self, task: TaskWidget):
        self.list_layout.addWidget(task)
