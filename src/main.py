import sys
from PyQt5.QtWidgets import QApplication, QDialog
from ui import Ui_Dialog
from PyQt5.QtWidgets import QApplication, QWidget, QLabel
from PyQt5.QtGui import QIcon, QPixmap
from PyQt5.QtCore import Qt
from guessed_screenshot import GuessedScreenshot


def show_random_screenshot():
    pixmap = QPixmap(screenshot.get_screenshot())
    w, h = ui.pic_label.width(), ui.pic_label.height()

    ui.pic_label.setPixmap(pixmap.scaled(w, h, Qt.KeepAspectRatio))
    ui.movieName.setText(screenshot.get_name())


app = QApplication(sys.argv)
window = QDialog()
ui = Ui_Dialog()
ui.setupUi(window)

screenshot = GuessedScreenshot()

show_random_screenshot()

window.show()
sys.exit(app.exec_())