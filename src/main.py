import sys
from PyQt5.QtWidgets import QApplication
import controller
from view import elements, windows

# create app
app = QApplication(sys.argv)

# create windows
main_menu = windows.MainMenuWindow()
game_window = windows.GameWindow()

# create elements
buttons = elements.AnswerButtons()

# create controllers
game_controller = controller.GameController((game_window.ui.pic_label.width(), game_window.ui.pic_label.height()))
ui_controller = controller.UIController()

# setup objects
buttons.addButton(game_window.ui.pushButton, 0)
buttons.addButton(game_window.ui.pushButton_2, 1)
buttons.addButton(game_window.ui.pushButton_3, 2)
buttons.addButton(game_window.ui.pushButton_4, 3)

# connect signals to slots
game_controller.screenshot_changed.connect(game_window.ui.pic_label.setPixmap)
game_controller.score_changed.connect(game_window.ui.score.setNum)
game_controller.answer_options_changed.connect(buttons.change_labels)

buttons.buttonClicked[int].connect(game_controller.choose_answer)

ui_controller.hide_main_menu.connect(main_menu.hide)
ui_controller.show_game_window.connect(game_window.show)

main_menu.ui.newGameButton.clicked.connect(ui_controller.new_game)

# start app
game_controller.change_state()
main_menu.show()
sys.exit(app.exec_())