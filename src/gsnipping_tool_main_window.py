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
        
        self.new_screenshot_button = QPushButton()
        self.cancel_screenshot_button = QPushButton()
        self.options_button = QPushButton()
        
        self.main_layout.addWidget(self.new_screenshot_button)
        self.main_layout.addWidget(self.cancel_screenshot_button)
        self.main_layout.addWidget(self.options_button)
        
        self.setCentralWidget(self.main_widget)

app = QApplication(sys.argv)

window = GSnippingToolMainWindow()
window.show()

app.exec()