import winreg
from pynput import keyboard
from PyQt6.QtWidgets import QApplication, QMainWindow
from PyQt6.QtCore import QThread, pyqtSignal, Qt
from gsnipping_tool_capture import GSnippingToolCapture

def add_to_registry() -> None:
    key = winreg.OpenKey(winreg.HKEY_CURRENT_USER, "Software\\Microsoft\\Windows\\CurrentVersion\\Run", 0, winreg.KEY_ALL_ACCESS)
    winreg.SetValueEx(key, "gsnipping_tool_reg", 0, winreg.REG_SZ, "C:\\Program Files (x86)\\Common Files\\GSnipping-Tool\\gsnipping_tool_background_shortcuts.exe")
    key.Close()


class SnippingToolCaptureApp(QMainWindow):
    trigger_full_snip = pyqtSignal()
    trigger_rect_snip = pyqtSignal()
    trigger_alt_tab = pyqtSignal()
    trigger_cmd_tab = pyqtSignal()
    trigger_esc = pyqtSignal()

    def __init__(self) -> None:
        super().__init__()
        self.hide()
        self.setWindowOpacity(0.0)
        self.setWindowFlags(Qt.WindowType.FramelessWindowHint | Qt.WindowType.Tool)
        self.capture = None

        self.trigger_full_snip.connect(self.full_screen_snip)
        self.trigger_rect_snip.connect(self.rectangle_snip)
        self.trigger_alt_tab.connect(self.close_capture)
        self.trigger_cmd_tab.connect(self.close_capture)
        self.trigger_esc.connect(self.close_capture)


    def full_screen_snip(self) -> None:
        print("Full screen snip triggered.")
        self.capture = GSnippingToolCapture(self, True)
        self.capture.show()
        self.hide()


    def rectangle_snip(self) -> None:
        print("Rectangle snip triggered.")
        self.capture = GSnippingToolCapture(self)
        self.capture.show()
        self.hide()


    def close_capture(self) -> None:
        print("Close capture triggered.")
        if self.capture:
            self.capture.close()


class HotkeyListener(QThread):
    full_snip = pyqtSignal()
    rect_snip = pyqtSignal()
    alt_tab = pyqtSignal()
    cmd_tab = pyqtSignal()

    def __init__(self) -> None:
        super(HotkeyListener, self).__init__()
        

    def run(self) -> None:
        hotkeys = keyboard.GlobalHotKeys(
            {
                '<alt>+f': self.full_snip.emit,
                '<alt>+s': self.rect_snip.emit,
                '<alt>+<tab>': self.alt_tab.emit,
                '<cmd>+<tab>': self.cmd_tab.emit,
            }
        )
        hotkeys.start()
        hotkeys.join()


class KeyListener(QThread):
    esc = pyqtSignal()

    def __init__(self) -> None:
        super(KeyListener, self).__init__()


    def run(self) -> None:
        listener = keyboard.Listener(
            on_press=self.on_press,
        )
        listener.start()
        listener.join()
    

    def on_press(self, key) -> None:
        if key == keyboard.Key.esc:
            print("ESC key pressed.")
            self.esc.emit()
            return True
        return False


def main() -> None:
    app = QApplication([])

    add_to_registry()

    main_window = SnippingToolCaptureApp()

    hotkeys_listener_thread = HotkeyListener()
    hotkeys_listener_thread.full_snip.connect(main_window.trigger_full_snip)
    hotkeys_listener_thread.rect_snip.connect(main_window.trigger_rect_snip)
    hotkeys_listener_thread.alt_tab.connect(main_window.trigger_alt_tab)
    hotkeys_listener_thread.cmd_tab.connect(main_window.trigger_cmd_tab)

    keys_listener_thread = KeyListener()
    keys_listener_thread.esc.connect(main_window.trigger_esc)
    
    keys_listener_thread.start()
    hotkeys_listener_thread.start()

    main_window.show()
    app.exec()


if __name__ == "__main__":
    main()
