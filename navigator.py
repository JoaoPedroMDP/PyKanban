#  coding: utf-8
from PyQt5.QtWidgets import QStackedWidget

from screens.LoginScreen import LoginScreen
from screens.RegisterScreen import RegisterScreen
from screens.TableScreen import TableScreen


class Navigator:
    SCREENS = {
        "login": LoginScreen,
        "register": RegisterScreen,
        "table": TableScreen
    }

    def __init__(self):
        self.stack = QStackedWidget()

    def navigate(self, screen: str, data: dict = None):
        screen = self.SCREENS[screen](self, data)
        self.stack.removeWidget(self.stack.currentWidget())
        self.stack.addWidget(screen)
        self.stack.setGeometry(self.stack.currentWidget().geometry())
