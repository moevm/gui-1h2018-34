import sys
from ui import Ui_Dialog
from PyQt5.QtWidgets import QApplication, QDialog
import controller
import view

app = QApplication(sys.argv)
window = QDialog()
ui = Ui_Dialog()
ui.setupUi(window)

game_controller = controller.GameController((ui.pic_label.width(), ui.pic_label.height()))
game_controller.screenshot_changed.connect(ui.pic_label.setPixmap)


buttons = view.AnswerButtons()
buttons.addButton(ui.pushButton, 0)
buttons.addButton(ui.pushButton_2, 1)
buttons.addButton(ui.pushButton_3, 2)
buttons.addButton(ui.pushButton_4, 3)

buttons.buttonClicked[int].connect(game_controller.choose_answer)
game_controller.answer_options_changed.connect(buttons.change_labels)

game_controller.change_state()

window.show()
sys.exit(app.exec_())