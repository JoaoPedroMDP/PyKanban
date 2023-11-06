#  coding: utf-8
from PyQt5.QtWidgets import QMainWindow
from PyQt5.uic import loadUi

from memory import USERS


class LoginScreen(QMainWindow):
    def __init__(self, navigator):
        super(LoginScreen, self).__init__()
        loadUi("screens/raw_screens/LoginScreen.ui", self)
        self.navigator = navigator
        self.confirm_button.released.connect(self.login)
        self.register_button.released.connect(lambda: self.navigator.navigate("register"))

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

        print(user["name"])
