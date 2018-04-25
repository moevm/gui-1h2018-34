from PyQt5.QtWidgets import QButtonGroup, QLabel
from PyQt5.QtCore import QTimer, pyqtSlot, pyqtSignal, QObject, Qt
from PyQt5.QtGui import QResizeEvent


class AnswerButtons(QButtonGroup):
    def __init__(self):
        super(AnswerButtons, self).__init__()

    @pyqtSlot(list)
    def change_labels(self, labels):
        for button, label in zip(self.buttons(), labels):
            button.setText(label)

    def change_colors(self, colors):
        pass


class Screenshot(QLabel):
    def __init__(self, *args, **kwargs):
        super(Screenshot, self).__init__(*args, **kwargs)
        self.__screenshot = None

    @pyqtSlot("QPixmap")
    def set_screenshot(self, screenshot):
        self.__screenshot = screenshot
        self.setPixmap(self.__screenshot.scaled(self.width(), self.height(), Qt.KeepAspectRatio))

    def resizeEvent(self, a0: QResizeEvent):
        super(Screenshot, self).resizeEvent(a0)
        if self.__screenshot is not None:
            self.setPixmap(self.__screenshot.scaled(self.width(), self.height(), Qt.KeepAspectRatio))