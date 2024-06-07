import ctypes
from PyQt6.QtGui import *
from PyQt6.QtWidgets import *
from PyQt6.QtCore import *
from consts import *
from functools import partial
import time
from gsnipping_tool_screenshoter import GSnippingToolScreenShoter

class GSnippingToolMainWindow(QMainWindow):
    def __init__(self, *args, **kwargs) -> None:
        super(GSnippingToolMainWindow, self).__init__(*args, **kwargs)
        
        self.__screen_shoter = GSnippingToolScreenShoter()
        
        self.setWindowTitle("GSnipping Tool")
        self.setWindowIcon(QIcon("./icons/icon.png"))
        
        self.main_widget = QWidget()
        self.main_layout = QHBoxLayout()
        self.main_widget.setLayout(self.main_layout)
        
        self.toolbar = QToolBar()
        self.toolbar.setToolButtonStyle(Qt.ToolButtonStyle.ToolButtonTextBesideIcon)
        self.addToolBar(self.toolbar)
        
        self.new_button_action = QAction(QIcon("./icons/new.png"), "New", self)
        self.new_button_action.triggered.connect(partial(self.__new_button_action_callback))
        
        self.mode_menu = QMenu()
        self.snip_actions = {
            FULL_SCREEN_SNIP_ACTION : self.mode_menu.addAction("Full-screen Snip"),
            RECTANGLE_SNIP_ACTION : self.mode_menu.addAction("Rectangle Snip"),
        }

        self.__set_all_actions_checkable(self.snip_actions)
        self.snip_actions[FULL_SCREEN_SNIP_ACTION].setChecked(True)

        self.mode_tool_button = QToolButton(self.toolbar)
        self.mode_tool_button.setText("Mode")
        self.mode_tool_button.setIcon(QIcon("./icons/mode.png"))
        self.mode_tool_button.setToolButtonStyle(Qt.ToolButtonStyle.ToolButtonTextBesideIcon)
        self.mode_tool_button.setMenu(self.mode_menu)
        self.mode_tool_button.setPopupMode(QToolButton.ToolButtonPopupMode.MenuButtonPopup)
        
        self.delay_menu = QMenu()
        
        self.delay_actions = {
            NO_DELAY_ACTION : self.delay_menu.addAction('No Delay'),
            ONE_SECOND_DELAY_ACTION : self.delay_menu.addAction('1 Second'),
            TWO_SECONDS_DELAY_ACTION : self.delay_menu.addAction('2 Seconds'),
            THREE_SECONDS_DELAY_ACTION : self.delay_menu.addAction('3 Seconds'),
            FOUR_SECONDS_DELAY_ACTION : self.delay_menu.addAction('4 Seconds'),
            FIVE_SECONDS_DELAY_ACTION : self.delay_menu.addAction('5 Seconds'),
        }
        
        self.delay_values = {
            NO_DELAY_ACTION : 0,
            ONE_SECOND_DELAY_ACTION : 1,
            TWO_SECONDS_DELAY_ACTION : 2,
            THREE_SECONDS_DELAY_ACTION : 3,
            FOUR_SECONDS_DELAY_ACTION : 4,
            FIVE_SECONDS_DELAY_ACTION : 5,
        }
        
        self.__set_all_actions_checkable(self.delay_actions)
        self.delay_actions[NO_DELAY_ACTION].setChecked(True)
        
        self.delay_tool_button = QToolButton(self.toolbar)
        self.delay_tool_button.setText("Delay")
        self.delay_tool_button.setIcon(QIcon("./icons/delay.png"))
        self.delay_tool_button.setToolButtonStyle(Qt.ToolButtonStyle.ToolButtonTextBesideIcon)
        self.delay_tool_button.setMenu(self.delay_menu)
        self.delay_tool_button.setPopupMode(QToolButton.ToolButtonPopupMode.MenuButtonPopup)
        
        self.cancel_button_action = QAction(QIcon("./icons/cancel.png"), "Cancel", self)
        self.cancel_button_action.triggered.connect(lambda: print('Pressed Cancel'))
        self.cancel_button_action.setDisabled(True)
        
        self.options_button_action = QAction(QIcon("./icons/options.png"), "Options", self)
        self.options_button_action.triggered.connect(lambda: print('Options Pressed'))
        
        self.toolbar.addAction(self.new_button_action)
        self.toolbar.addWidget(self.mode_tool_button)
        self.toolbar.addWidget(self.delay_tool_button)
        self.toolbar.addAction(self.cancel_button_action)
        self.toolbar.addAction(self.options_button_action)
        
        self.setCentralWidget(self.main_widget)
    
    
    def __set_all_actions_checkable(self, actions: dict[QAction]) -> None:
        for action in actions.keys():
            actions[action].setCheckable(True)
            actions[action].triggered.connect(partial(self.__check_action, actions[action], actions))
            
    
    def __check_action(self, action: QAction, actions: dict[QAction]) -> None:
        if not action.isChecked():
            action.setChecked(True)
        
        for other_action in actions.keys():
            if actions[other_action] != action:
                actions[other_action].setChecked(False)
            
    
    def __new_button_action_callback(self) -> None:
        delay = 0
        snip_mode = ''
        
        for action in self.delay_actions.keys():
            if self.delay_actions[action].isChecked():
                delay = self.delay_values[action]
                break
        
        for action in self.snip_actions.keys():
            if self.snip_actions[action].isChecked():
                snip_mode = action
                break
        
        self.cancel_button_action.setEnabled(True)
        
        self.hide()
        
        time.sleep(delay)
        
        if FULL_SCREEN_SNIP_ACTION == snip_mode:
            self.__screen_shoter.take_screenshot()
            
        self.show()
        
        self.cancel_button_action.setDisabled(True)