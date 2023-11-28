#  coding: utf-8
import signal
import sys

from PyQt5.QtWidgets import QApplication

from memory import load_memory, save_memory
from navigator import Navigator


def close_program(*args):
    save_memory()
    sys.exit(0)


def main():
    load_memory()
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
