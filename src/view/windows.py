from PyQt5.QtWidgets import QWidget
from view.uis import main_menu, game


class MainMenuWindow(QWidget):
    def __init__(self, parent=None):
        QWidget.__init__(self, parent)
        self.ui = main_menu.Ui_Form()
        self.ui.setupUi(self)


class GameWindow(QWidget):
    def __init__(self, parent=None):
        QWidget.__init__(self, parent)
        self.ui = game.Ui_Dialog()
        self.ui.setupUi(self)