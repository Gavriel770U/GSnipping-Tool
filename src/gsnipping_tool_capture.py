from PyQt6.QtWidgets import QApplication, QMainWindow, QPushButton, QWidget
from PyQt6.QtGui import QPainter, QGuiApplication, QPen
from PyQt6.QtCore import Qt, QRect
import time

class GSnippingToolCapture(QWidget):
    def __init__(self) -> None:
        super().__init__()
        self.setWindowTitle("Snipping Tool")
        self.setWindowFlags(Qt.WindowType.FramelessWindowHint | Qt.WindowType.WindowStaysOnTopHint)
        self.setWindowState(Qt.WindowState.WindowFullScreen)
        self.setWindowOpacity(0.3)
        self.begin = None
        self.end = None
        
        time.sleep(0.2)
        
        QApplication.setOverrideCursor(Qt.CursorShape.CrossCursor)
        
        self.setMouseTracking(True)

    def paintEvent(self, event) -> None:
        if self.begin and self.end:
            qp = QPainter(self)
            qp.setPen(QPen(Qt.GlobalColor.black, 3, Qt.PenStyle.SolidLine))
            rect = self.get_rectangle()
            qp.drawRect(rect)


    def mousePressEvent(self, event) -> None:
        self.begin = event.pos()
        self.end = self.begin
        self.update()


    def mouseMoveEvent(self, event) -> None:
        self.end = event.pos()
        self.update()


    def mouseReleaseEvent(self, event) -> None:
        self.close()
        self.capture_snip()
        QApplication.restoreOverrideCursor()
        
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