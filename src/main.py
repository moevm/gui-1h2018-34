import sys
from ui import Ui_Dialog
from main_menu import Ui_Form as MainMenu
from PyQt5.QtWidgets import QApplication, QDialog, QWidget
import controller
import view

app = QApplication(sys.argv)
window = QDialog()
ui = Ui_Dialog()
ui.setupUi(window)

window2 = QWidget()
main_menu = MainMenu()
main_menu.setupUi(window2)

game_controller = controller.GameController((ui.pic_label.width(), ui.pic_label.height()))
game_controller.screenshot_changed.connect(ui.pic_label.setPixmap)
game_controller.score_changed.connect(ui.score.setNum)

buttons = view.AnswerButtons()
buttons.addButton(ui.pushButton, 0)
buttons.addButton(ui.pushButton_2, 1)
buttons.addButton(ui.pushButton_3, 2)
buttons.addButton(ui.pushButton_4, 3)
buttons.buttonClicked[int].connect(game_controller.choose_answer)

game_controller.answer_options_changed.connect(buttons.change_labels)
game_controller.change_state()

ui_controller = controller.UIController()
ui_controller.hide_main_menu.connect(window2.hide)
ui_controller.show_game_window.connect(window.show)
main_menu.newGameButton.clicked.connect(ui_controller.new_game)


window2.show()
sys.exit(app.exec_())