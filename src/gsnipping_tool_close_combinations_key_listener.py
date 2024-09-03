from PyQt6.QtCore import QThread, pyqtSignal
from pynput import keyboard
from consts import *

class GSnippingToolCloseCombinationsKeyListener(QThread):
    key_pressed = pyqtSignal(object)
    key_released = pyqtSignal(object)
    
    def __init__(self, parent=None) -> None:
        super(GSnippingToolCloseCombinationsKeyListener, self).__init__(parent)
        
        self.__close_combinations = [
            ESC_COMBINATION,
            CMD_COMBINATION,
            LALT_TAB_COMBINATION,
            CMD_TAB_COMBINATION,
        ]
        
        self.__current = set()
        
        
    def run(self) -> None:
        with keyboard.Listener(on_press=self.__on_press, on_release=self.__on_release) as listener:
            listener.join()
    
    
    def __on_press(self, key) -> None:
        if any([key in combination for combination in self.__close_combinations]):
            self.__current.add(key)
            if any(all(k in self.__current for k in combination) for combination in self.__close_combinations):
                self.key_pressed.emit(key)
    
    
    def __on_release(self, key) -> None:
        if any([key in combination for combination in self.__close_combinations]):
            self.__current.remove(key)
            self.key_released.emit(key)