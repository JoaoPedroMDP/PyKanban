#  coding: utf-8
from PyQt5.QtWidgets import QStackedWidget

from qt_uis.screens.login_screen import LoginScreen
from qt_uis.screens.new_table_screen import NewTableScreen
from qt_uis.screens.register_screen import RegisterScreen
from qt_uis.screens.table_screen import TableScreen


class Navigator:
    SCREENS = {
        "login": LoginScreen,
        "register": RegisterScreen,
        "table": TableScreen,
        "new_table": NewTableScreen
    }

    def __init__(self):
        self.stack = QStackedWidget()
        self.user = None

    def login_user(self, user: dict):
        self.user = user

    def navigate(self, screen: str, data: dict = None):
        screen = self.SCREENS[screen](self, data)
        self.stack.removeWidget(self.stack.currentWidget())
        self.stack.addWidget(screen)
        self.stack.setGeometry(self.stack.currentWidget().geometry())
