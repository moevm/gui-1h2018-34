from PyQt5.QtCore import pyqtSlot, pyqtSignal, QObject, Qt
from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import QMessageBox
import model


class GameController(QObject):
    # Signals
    screenshot_changed = pyqtSignal("QPixmap")
    answer_options_changed = pyqtSignal(list)
    score_changed = pyqtSignal(int)

    def __init__(self, image_size, parent=None):
        QObject.__init__(self, parent)
        self.image_size = image_size
        self.picked_movies = None

        self.picker = model.MoviesPicker()
        self.score = model.Score()

    def __game_over(self):
        dialog = QMessageBox()
        dialog.setText("Game Over\n Your sore: {}".format(self.score.get_score()))
        dialog.exec()
        self.score.clear_score()
        self.picker.clear_picked_movies_history()


    @pyqtSlot(int)
    def choose_answer(self, answer_id):
        if self.picked_movies.get_answer_options()[answer_id] is self.picked_movies.get_answer():
            self.score.add_points(1)
        else:
            self.__game_over()

        self.score_changed.emit(self.score.get_score())
        self.change_state()

    @pyqtSlot()
    def change_state(self):
        self.picked_movies = self.picker.pick_movies(model.Difficult.EASY)
        answer = self.picked_movies.get_answer()

        pixmap = QPixmap(answer.get_screenshot())
        w, h = self.image_size
        pixmap = pixmap.scaled(w, h, Qt.KeepAspectRatio)

        self.screenshot_changed.emit(pixmap)
        self.answer_options_changed.emit(
            [answer.get_title() for answer in self.picked_movies.get_answer_options()])


class UIController(QObject):
    show_game_window = pyqtSignal()
    hide_main_menu = pyqtSignal()

    def __init__(self, parent=None):
        QObject.__init__(self, parent)

    @pyqtSlot()
    def new_game(self):
        self.hide_main_menu.emit()
        self.show_game_window.emit()
