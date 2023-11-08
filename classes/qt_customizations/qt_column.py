#  coding: utf-8
import pickle

from PyQt5.QtCore import Qt
from PyQt5.QtGui import QDropEvent, QDragLeaveEvent
from PyQt5.QtWidgets import QListWidget, QWidget

from classes.Column import Column


class QtColumn(QListWidget):
    def __init__(self, parent: QWidget, column: Column):
        super(QtColumn, self).__init__(parent)
        # Configurando a possibilidade de a pessoa arrastar uma tarefa para outra coluna
        self.setSelectionMode(QListWidget.SingleSelection)
        self.setDragEnabled(True)
        self.viewport().setAcceptDrops(True)
        self.setDefaultDropAction(Qt.MoveAction)
        self.column = column

    def dropEvent(self, event: QDropEvent):
        super(QtColumn, self).dropEvent(event)
        print(event.mimeData().data("plain/text"))
        # self.column.add_task(event.source().task)

    def dragLeaveEvent(self, event: QDragLeaveEvent):
        print(event)
