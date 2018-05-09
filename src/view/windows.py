from PyQt5.QtWidgets import QWidget, QDialog
from view.uis import main_menu, difficult_menu, game, records, pause_menu, game_over_menu
from view.elements import RecordsTable
import model
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

        self.ui.scrollArea_1.setWidget(RecordsTable(model.Difficult.EASY))
        self.ui.scrollArea_2.setWidget(RecordsTable(model.Difficult.NORMAL))
        self.ui.scrollArea_3.setWidget(RecordsTable(model.Difficult.HARD))


class GameOverWindow(QDialog):
    name_entered = pyqtSignal(str)

    def __init__(self, score: model.Score, parent=None):
        QDialog.__init__(self, parent)
        self.ui = game_over_menu.Ui_Dialog()
        self.ui.setupUi(self)

        self.score = score
        self.ui.score.setText(str(score.get_score()))
        self.ui.pushButton.pressed.connect(self.accept)

    def accept(self):
        self.name_entered.emit(self.ui.name_textbox.text())
        super().accept()
