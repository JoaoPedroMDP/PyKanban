#  coding: utf-8
from PyQt5.QtWidgets import QMainWindow
from PyQt5.uic import loadUi

from memory import USERS


class RegisterScreen(QMainWindow):
    def __init__(self, navigator):
        super(RegisterScreen, self).__init__()
        self.navigator = navigator
        loadUi("screens/raw_screens/RegisterScreen.ui", self)
        self.register_button.released.connect(self.register)
        self.back_to_login_button.released.connect(lambda: self.navigator.navigate("login"))

    def reset_status_bar(self):
        self.statusbar.showMessage("")

    def set_status_bar(self, text: str):
        self.statusBar().showMessage(text)

    def register(self):
        new_user = {
            "name": self.name_input.text(),
            "login": self.login_input.text(),
            "password": self.password_input.text()
        }
        print(new_user)
        USERS.append(new_user)
        self.navigator.navigate("login")
