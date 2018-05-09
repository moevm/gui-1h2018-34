from PyQt5.QtWidgets import QWidget, QDialog
from view.uis import main_menu, difficult_menu, game, records, pause_menu
from view.elements import RecordsTable
from model import Difficult
from PyQt5.QtCore import pyqtSlot, pyqtSignal, pyqtSlot, QObject, Qt
from PyQt5.QtGui import QKeySequence

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
    exit_to_main_menu = pyqtSignal()

    def __init__(self, parent=None):
        QWidget.__init__(self, parent)
        self.ui = game.Ui_Dialog()
        self.ui.setupUi(self)

    def keyPressEvent(self, event):
        if event.matches(QKeySequence.Cancel):
            pause_window = QDialog()
            ui = pause_menu.Ui_Dialog()
            ui.setupUi(pause_window)

            pause_window.setModal(True)
            pause_window.exec()
            if pause_window.result() == QDialog.Rejected:
                self.exit_to_main_menu.emit()


class RecordsWindow(QWidget):
    def __init__(self, parent=None):
        QWidget.__init__(self, parent)
        self.ui = records.Ui_Form()
        self.ui.setupUi(self)

        self.ui.scrollArea_1.setWidget(RecordsTable(Difficult.EASY))
        self.ui.scrollArea_2.setWidget(RecordsTable(Difficult.NORMAL))
        self.ui.scrollArea_3.setWidget(RecordsTable(Difficult.HARD))