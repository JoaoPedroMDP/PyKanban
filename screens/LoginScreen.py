#  coding: utf-8
from PyQt5 import QtCore
from PyQt5.QtGui import QKeyEvent
from PyQt5.QtWidgets import QMainWindow
from PyQt5.uic import loadUi

from memory import USERS
from screens.raw_screens.LoginScreen import Ui_LoginScreen


class LoginScreen(QMainWindow, Ui_LoginScreen):
    def __init__(self, navigator, data: dict):
        super(LoginScreen, self).__init__()
        loadUi("screens/raw_screens/LoginScreen.ui", self)
        self.navigator = navigator
        self.confirm_button.released.connect(self.login)
        self.register_button.released.connect(lambda: self.navigator.navigate("register"))

    def keyReleaseEvent(self, event: QKeyEvent):
        if event.key() == QtCore.Qt.Key.Key_Return:
            self.login()

    def reset_status_bar(self):
        self.statusbar.showMessage("")

    def set_status_bar(self, text: str):
        self.statusBar().showMessage(text)

    def login(self):
        self.reset_status_bar()
        user = list(filter(lambda item: item["login"] == self.login_input.text(), USERS))
        if not user:
            self.set_status_bar("Usuário não encontrado")
            return

        user = user[0]
        if user["password"] != self.password_input.text():
            self.set_status_bar("Senha incorreta")
            return

        self.navigator.navigate("table", {"user": user})
