from PyQt6.QtWidgets import QApplication, QWidget
from PyQt6.QtGui import QPainter, QGuiApplication, QPen
from PyQt6.QtCore import Qt, QRect, QTimer
import time

class GSnippingToolCapture(QWidget):
    def __init__(self, main_window, is_full_screen: bool = False) -> None:
        super().__init__()
        self.setWindowTitle("Snipping Tool")
        self.setWindowFlags(Qt.WindowType.FramelessWindowHint | Qt.WindowType.WindowStaysOnTopHint | Qt.WindowType.Tool)
        self.setWindowState(Qt.WindowState.WindowFullScreen)
        self.setWindowOpacity(0.3)
        self.begin = None
        self.end = None
        
        self.__main_window = main_window
        self.__is_full_screen = is_full_screen
        
        time.sleep(0.2)
        
        QApplication.setOverrideCursor(Qt.CursorShape.CrossCursor)
        
        self.setMouseTracking(True)

        if self.__is_full_screen:
            QTimer.singleShot(100, self.capture_full_screen_and_exit)


    def paintEvent(self, event) -> None:
        if self.begin and self.end:
            qp = QPainter(self)
            qp.setPen(QPen(Qt.GlobalColor.black, 3, Qt.PenStyle.SolidLine))
            rect = self.get_rectangle()
            qp.drawRect(rect)


    def mousePressEvent(self, event) -> None:
        if self.__is_full_screen:
            return
        self.begin = event.pos()
        self.end = self.begin
        self.update()


    def mouseMoveEvent(self, event) -> None:
        if self.__is_full_screen:
            return
        self.end = event.pos()
        self.update()


    def mouseReleaseEvent(self, event) -> None:
        if self.__is_full_screen:
            return
        self.close()
        self.capture_snip()
        QApplication.restoreOverrideCursor()
        if self.__main_window:
            self.__main_window.show()
        
        
    def get_rectangle(self) -> QRect:
        if not self.begin or not self.end:
            return QRect()
        x1 = min(self.begin.x(), self.end.x())
        y1 = min(self.begin.y(), self.end.y())
        x2 = max(self.begin.x(), self.end.x())
        y2 = max(self.begin.y(), self.end.y())
        return QRect(x1, y1, x2 - x1, y2 - y1)


    def capture_snip(self) -> None:
        screen = QGuiApplication.primaryScreen()
        if not screen:
            return
        
        rect = self.get_rectangle()
        screenshot = screen.grabWindow(0, rect.left(), rect.top(), rect.width(), rect.height())
        screenshot.save("./snip.png", "png")
        clipboard = QGuiApplication.clipboard()
        clipboard.setPixmap(screenshot)
    
    
    def capture_full_screen_and_exit(self) -> None:
        self.hide()
        QTimer.singleShot(100, self.take_full_screen_shot)


    def take_full_screen_shot(self) -> None:
        screen = QGuiApplication.primaryScreen()
        if not screen:
            return

        screenshot = screen.grabWindow(0)
        screenshot.save("./snip.png", "png")
        clipboard = QGuiApplication.clipboard()
        clipboard.setPixmap(screenshot)
        QApplication.restoreOverrideCursor()
        if self.__main_window:
            self.__main_window.show()
        self.close()

