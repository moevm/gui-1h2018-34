from PyQt5.QtWidgets import QButtonGroup
from PyQt5.QtCore import QTimer, pyqtSlot, pyqtSignal, QObject, Qt


class AnswerButtons(QButtonGroup):
    def __init__(self):
        super(AnswerButtons, self).__init__()

    @pyqtSlot(list)
    def change_labels(self, labels):
        for button, label in zip(self.buttons(), labels):
            button.setText(label)

    def change_colors(self, colors):
        pass



