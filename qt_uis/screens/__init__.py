#  coding: utf-8


class HasStatusBar:
    def reset_status_bar(self):
        self.statusbar.showMessage("")

    def set_status_bar(self, text: str):
        self.statusBar().showMessage(text)
