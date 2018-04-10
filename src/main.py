import sys
from ui import Ui_Dialog
from PyQt5.QtWidgets import QApplication, QDialog
from PyQt5.QtGui import QPixmap
from PyQt5.QtCore import Qt
import model


def show_random_screenshot():
    pixmap = QPixmap(picked_movie.get_random_screenshot())
    w, h = ui.pic_label.width(), ui.pic_label.height()

    ui.pic_label.setPixmap(pixmap.scaled(w, h, Qt.KeepAspectRatio))
    ui.movieName.setText(picked_movie.get_title())


app = QApplication(sys.argv)
window = QDialog()
ui = Ui_Dialog()
ui.setupUi(window)

picker = model.PickedMovies()
picker.pick_movie(1)
picked_movie = picker.get_picked_movie()


show_random_screenshot()

window.show()
sys.exit(app.exec_())