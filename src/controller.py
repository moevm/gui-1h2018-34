import model
from PyQt5.QtCore import QTimer, pyqtSlot, pyqtSignal, QObject, Qt
from PyQt5.QtGui import QPixmap


class GameController(QObject):
    screenshot_changed = pyqtSignal("QPixmap")
    title_changed = pyqtSignal("QString")

    def __init__(self, image_size, parent=None):
        QObject.__init__(self, parent)
        self.picker = model.MoviesPicker()

        self.timer = QTimer()
        self.timer.timeout.connect(self.change_state)
        self.timer.start(5000)

        self.image_size = image_size

    @pyqtSlot()
    def change_state(self):
        picked_movies = self.picker.pick_movies(difficult=1)
        answer = picked_movies.get_answer()

        pixmap = QPixmap(answer.get_screenshot())
        w, h = self.image_size
        pixmap.scaled(w, h, Qt.KeepAspectRatio)

        self.screenshot_changed.emit(pixmap)
        self.title_changed.emit(answer.get_title())



