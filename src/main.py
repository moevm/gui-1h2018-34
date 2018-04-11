import sys
from ui import Ui_Dialog
from PyQt5.QtWidgets import QApplication, QDialog
import controller


app = QApplication(sys.argv)
window = QDialog()
ui = Ui_Dialog()
ui.setupUi(window)

game_controller = controller.GameController()
game_controller.screenshot_changed.connect(ui.pic_label.setPixmap)
game_controller.title_changed.connect(ui.movieName.setText)

game_controller.change_state()

window.show()
sys.exit(app.exec_())