import model
from PyQt5.QtCore import QTimer, pyqtSlot, pyqtSignal, QObject
from PyQt5.QtGui import QPixmap


class GameController(QObject):
    screenshot_changed = pyqtSignal("QPixmap")
    title_changed = pyqtSignal("QString")

    def __init__(self, parent=None):
        QObject.__init__(self, parent)
        self.picker = model.MoviesPicker()

        self.timer = QTimer()
        self.timer.timeout.connect(self.change_state)
        self.timer.start(5000)

    @pyqtSlot()
    def change_state(self):
        picked_movies = self.picker.pick_movies(difficult=1)
        answer = picked_movies.get_answer()

        pixmap = QPixmap(answer.get_screenshot())
        self.screenshot_changed.emit(pixmap)
        self.title_changed.emit(answer.get_title())



