import winreg
from pynput import keyboard
from gsnipping_tool_capture import GSnippingToolCapture
from PyQt6.QtWidgets import QApplication, QMainWindow
from PyQt6.QtCore import QThread, pyqtSignal, Qt

def add_to_registry() -> None:
    key = winreg.OpenKey(winreg.HKEY_CURRENT_USER, "Software\\Microsoft\\Windows\\CurrentVersion\\Run", 0, winreg.KEY_ALL_ACCESS)
    winreg.SetValueEx(key, "gsnipping_tool_reg", 0, winreg.REG_SZ, "C:\\Program Files (x86)\\Common Files\\GSnipping-Tool\\gsnipping_tool_background_shortcuts.exe")
    key.Close()
    

class SnippingToolCaptureApp(QMainWindow):
    trigger_full_snip = pyqtSignal()
    trigger_rect_snip = pyqtSignal()

    def __init__(self) -> None:
        super().__init__()
        self.hide()
        self.setWindowOpacity(0.0)
        self.setWindowFlags(Qt.WindowType.FramelessWindowHint)
        self.trigger_full_snip.connect(self.full_screen_snip)
        self.trigger_rect_snip.connect(self.rectangle_snip)


    def full_screen_snip(self) -> None:
        self.capture = GSnippingToolCapture(self, True)
        self.capture.show()
        self.hide()


    def rectangle_snip(self) -> None:
        self.capture = GSnippingToolCapture(self)
        self.capture.show()
        self.hide()


class HotkeyListener(QThread):
    full_snip = pyqtSignal()
    rect_snip = pyqtSignal()

    def run(self) -> None:
        hotkeys = keyboard.GlobalHotKeys(
            {
                '<alt>+f': self.full_snip.emit,
                '<alt>+s': self.rect_snip.emit,
            }
        )
        hotkeys.start()
        hotkeys.join()


def main() -> None:
    app = QApplication([])

    add_to_registry()

    main_window = SnippingToolCaptureApp()

    listener_thread = HotkeyListener()
    listener_thread.full_snip.connect(main_window.trigger_full_snip)
    listener_thread.rect_snip.connect(main_window.trigger_rect_snip)
    listener_thread.start()

    main_window.show()
    app.exec()


if __name__ == "__main__":
    main()
