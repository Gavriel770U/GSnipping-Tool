from PyQt6.QtGui import *
from PyQt6.QtWidgets import *
from PyQt6.QtCore import *
import sys

class GSnippingToolMainWindow(QMainWindow):
    def __init__(self, *args, **kwargs) -> None:
        super(GSnippingToolMainWindow, self).__init__(*args, **kwargs)
        
        self.setWindowTitle("GSnipping Tool")
        
        self.main_widget = QWidget()
        self.main_layout = QHBoxLayout()
        self.main_widget.setLayout(self.main_layout)
        
        self.toolbar = QToolBar()
        self.toolbar.setToolButtonStyle(Qt.ToolButtonStyle.ToolButtonTextBesideIcon)
        self.addToolBar(self.toolbar)
        
        self.new_button_action = QAction(QIcon("./icons/new.png"), "New", self)
        self.new_button_action.triggered.connect(lambda: print('Pressed New'))
        self.new_button_action.setCheckable(True)
        
        self.cancel_button_action = QAction(QIcon("./icons/cancel.png"), "Cancel", self)
        self.cancel_button_action.triggered.connect(lambda: print('Pressed Cancel'))
        self.cancel_button_action.setCheckable(True)
        
        self.options_button_action = QAction(QIcon("./icons/options.png"), "Options", self)
        self.options_button_action.triggered.connect(lambda: print('Options Pressed'))
        self.options_button_action.setCheckable(True)
        
        self.toolbar.addAction(self.new_button_action)
        self.toolbar.addAction(self.cancel_button_action)
        self.toolbar.addAction(self.options_button_action)
        
        self.setCentralWidget(self.main_widget)

app = QApplication(sys.argv)

window = GSnippingToolMainWindow()
window.show()

app.exec()