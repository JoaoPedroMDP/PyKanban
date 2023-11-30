#  coding: utf-8
import signal
import sys

from PyQt5.QtWidgets import QApplication

from classes.pure.column import Column
from classes.pure.table import Table
from classes.pure.task import Task
from classes.pure.user import User
from navigator import Navigator


def close_program(*args):
    Task.save_memory()
    Column.save_memory()
    Table.save_memory()
    User.save_memory()
    return


def main():
    # Precisa ser task antes de column antes de table
    Task.load_memory()
    Column.load_memory()
    Table.load_memory()
    User.load_memory()

    signal.signal(signal.SIGINT, close_program)

    app = QApplication(sys.argv)
    app.setQuitOnLastWindowClosed(True)
    app.aboutToQuit.connect(close_program)

    navigator = Navigator()
    navigator.navigate("login")
    navigator.stack.show()

    app.exec()


if __name__ == '__main__':
    main()
