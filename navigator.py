#  coding: utf-8
from PyQt5.QtWidgets import QStackedWidget

from screens.LoginScreen import LoginScreen
from screens.RegisterScreen import RegisterScreen


class Navigator:
    SCREENS = {
        "login": LoginScreen,
        "register": RegisterScreen
    }

    def __init__(self):
        self.stack = QStackedWidget()

    def navigate(self, screen: str):
        screen = self.SCREENS[screen](self)
        self.stack.removeWidget(self.stack.currentWidget())
        self.stack.addWidget(screen)
        self.stack.setGeometry(self.stack.currentWidget().geometry())
