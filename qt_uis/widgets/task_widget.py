#  coding: utf-8
from PyQt5.QtCore import pyqtSignal
from PyQt5.QtWidgets import QWidget
from PyQt5.uic import loadUi

from classes.pure.Task import Task
from consts import FORWARD, BACKWARD
from qt_uis.widgets.raw_widgets.TaskWidget import Ui_TaskWidget


class TaskWidget(QWidget, Ui_TaskWidget):
    move_task = pyqtSignal(Task, int)

    def __init__(self, task: Task, parent=None):
        super(TaskWidget, self).__init__(parent)
        loadUi("qt_uis/widgets/raw_widgets/TaskWidget.ui", self)
        self.config_ui()
        self.task = task
        self.task_name_label.setText(task.name)
        self.send_task_button.released.connect(self.send_task)
        self.return_task_button.released.connect(self.return_task)

    def config_ui(self):
        # Para debugar apenas
        # self.setStyleSheet("background-color: #ff0000;")
        self.setMaximumWidth(self.parent().width())

    def send_task(self):
        self.move_task.emit(self.task, FORWARD)

    def return_task(self):
        self.move_task.emit(self.task, BACKWARD)
