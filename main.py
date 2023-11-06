#  coding: utf-8
import signal
import sys

from PyQt5.QtWidgets import QApplication

from navigator import Navigator

app = QApplication(sys.argv)
signal.signal(signal.SIGINT, signal.SIG_DFL)

navigator = Navigator()
navigator.navigate("login")
navigator.stack.show()
app.exec()
