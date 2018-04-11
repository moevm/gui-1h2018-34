import model
from PyQt5.QtCore import QTimer, pyqtSlot, pyqtSignal, QObject, Qt
from PyQt5.QtGui import QPixmap


class GameController(QObject):
    screenshot_changed = pyqtSignal("QPixmap")
    answer_options_changed = pyqtSignal(list)
    score_changed = pyqtSignal(int)

    def __init__(self, image_size, parent=None):
        QObject.__init__(self, parent)
        self.image_size = image_size

        self.picker = model.MoviesPicker()
        self.score = model.Score()

    @pyqtSlot(int)
    def choose_answer(self, answer_id):
        if self.picked_movies.get_answer_options()[answer_id] is self.picked_movies.get_answer():
            print('Correct')
            self.score.add_points(1)
        else:
            print("Not correct")
            self.score.clear_score()

        self.score_changed.emit(self.score.get_score())
        self.change_state()

    @pyqtSlot()
    def change_state(self):
        self.picked_movies = self.picker.pick_movies(difficult=1)
        answer = self.picked_movies.get_answer()

        pixmap = QPixmap(answer.get_screenshot())
        w, h = self.image_size
        pixmap.scaled(w, h, Qt.KeepAspectRatio)

        self.screenshot_changed.emit(pixmap)
        self.answer_options_changed.emit(
            [answer.get_title() for answer in self.picked_movies.get_answer_options()])



