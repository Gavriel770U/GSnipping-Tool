from PyQt6.QtGui import *
from PyQt6.QtWidgets import *
from PyQt6.QtCore import *
import sys

class GSnippingToolMainWindow(QMainWindow):
    def __init__(self, *args, **kwargs) -> None:
        super(GSnippingToolMainWindow, self).__init__(*args, **kwargs)
        
        self.setWindowTitle("GSnipping Tool")
        self.setWindowIcon(QIcon("./icons/icon.png"))
        
        self.main_widget = QWidget()
        self.main_layout = QHBoxLayout()
        self.main_widget.setLayout(self.main_layout)
        
        self.toolbar = QToolBar()
        self.toolbar.setToolButtonStyle(Qt.ToolButtonStyle.ToolButtonTextBesideIcon)
        self.addToolBar(self.toolbar)
        
        self.new_button_action = QAction(QIcon("./icons/new.png"), "New", self)
        self.new_button_action.triggered.connect(lambda: print('Pressed New'))
        self.new_button_action.setCheckable(True)
        
        self.mode_menu = QMenu()
        self.full_screen_snip_action = self.mode_menu.addAction("Full-screen Snip")
        self.rectangle_snip_action = self.mode_menu.addAction("Rectangle Snip")

        self.mode_tool_button = QToolButton(self.toolbar)
        self.mode_tool_button.setText("Mode")
        self.mode_tool_button.setIcon(QIcon("./icons/mode.png"))
        self.mode_tool_button.setToolButtonStyle(Qt.ToolButtonStyle.ToolButtonTextBesideIcon)
        self.mode_tool_button.setMenu(self.mode_menu)
        self.mode_tool_button.setPopupMode(QToolButton.ToolButtonPopupMode.MenuButtonPopup)
        self.mode_tool_button.setCheckable(True)
        
        self.delay_menu = QMenu()
        self.no_delay_action = self.delay_menu.addAction('No Delay')
        self.one_second_delay_action = self.delay_menu.addAction('1 Second')
        self.two_seconds_delay_action = self.delay_menu.addAction('2 Seconds')
        self.three_seconds_delay_action = self.delay_menu.addAction('3 Seconds')
        self.four_seconds_delay_action = self.delay_menu.addAction('4 Seconds')
        self.five_seconds_delay_action = self.delay_menu.addAction('5 Seconds')
        
        self.delay_tool_button = QToolButton(self.toolbar)
        self.delay_tool_button.setText("Delay")
        self.delay_tool_button.setIcon(QIcon("./icons/delay.png"))
        self.delay_tool_button.setToolButtonStyle(Qt.ToolButtonStyle.ToolButtonTextBesideIcon)
        self.delay_tool_button.setMenu(self.delay_menu)
        self.delay_tool_button.setPopupMode(QToolButton.ToolButtonPopupMode.MenuButtonPopup)
        self.delay_tool_button.setCheckable(True)
        
        self.cancel_button_action = QAction(QIcon("./icons/cancel.png"), "Cancel", self)
        self.cancel_button_action.triggered.connect(lambda: print('Pressed Cancel'))
        self.cancel_button_action.setCheckable(True)
        
        self.options_button_action = QAction(QIcon("./icons/options.png"), "Options", self)
        self.options_button_action.triggered.connect(lambda: print('Options Pressed'))
        self.options_button_action.setCheckable(True)
        
        self.toolbar.addAction(self.new_button_action)
        self.toolbar.addWidget(self.mode_tool_button)
        self.toolbar.addWidget(self.delay_tool_button)
        self.toolbar.addAction(self.cancel_button_action)
        self.toolbar.addAction(self.options_button_action)
        
        self.setCentralWidget(self.main_widget)

app = QApplication(sys.argv)

window = GSnippingToolMainWindow()
window.show()

app.exec()
