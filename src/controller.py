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

        self.change_state()

    @pyqtSlot()
    def change_state(self):
        self.picker.pick_movie(difficult=1)
        picked_movie = self.picker.get_picked_movie()

        pixmap = QPixmap(picked_movie.get_random_screenshot())
        self.screenshot_changed.emit(pixmap)
        self.title_changed.emit(picked_movie.get_title())
