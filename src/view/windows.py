from PyQt5.QtWidgets import QWidget
from view.uis import main_menu, difficult_menu, game, records
from PyQt5.QtCore import pyqtSlot, pyqtSignal, pyqtSlot, QObject, Qt

class MainMenuWindow(QWidget):
    def __init__(self, parent=None):
        QWidget.__init__(self, parent)
        self.ui = main_menu.Ui_Form()
        self.ui.setupUi(self)


class DifficultMenuWindow(QWidget):
    def __init__(self, parent=None):
        QWidget.__init__(self, parent)
        self.ui = difficult_menu.Ui_Form()
        self.ui.setupUi(self)


class GameWindow(QWidget):
    def __init__(self, parent=None):
        QWidget.__init__(self, parent)
        self.ui = game.Ui_Dialog()
        self.ui.setupUi(self)


class RecordsWindow(QWidget):
    def __init__(self, parent=None):
        QWidget.__init__(self, parent)
        self.ui = records.Ui_Form()
        self.ui.setupUi(self)