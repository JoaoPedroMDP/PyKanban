#  coding: utf-8
from PyQt5 import QtCore
from PyQt5.QtGui import QKeyEvent
from PyQt5.QtWidgets import QMainWindow
from PyQt5.uic import loadUi

from classes.pure.user import User
from qt_uis.screens import HasStatusBar


class LoginScreen(QMainWindow, HasStatusBar):
    def __init__(self, navigator, data: dict):
        super(LoginScreen, self).__init__()
        loadUi("qt_uis/screens/raw_screens/LoginScreen.ui", self)
        self.navigator = navigator
        self.confirm_button.released.connect(self.login)
        self.register_button.released.connect(lambda: self.navigator.navigate("register"))

    def keyReleaseEvent(self, event: QKeyEvent):
        if event.key() == QtCore.Qt.Key.Key_Return:
            self.login()

    def login(self):
        self.reset_status_bar()
        user = User.get_user_by_login(self.login_input.text())

        if not user:
            self.set_status_bar("Usuário não encontrado")
            return

        user = user
        if user.password != self.password_input.text():
            self.set_status_bar("Senha incorreta")
            return

        self.navigator.login_user(user)
