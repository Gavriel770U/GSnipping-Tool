from gsnipping_tool_main_window import GSnippingToolMainWindow
import sys
from PyQt6.QtWidgets import QApplication


def main() -> None:
    app = QApplication(sys.argv)

    window = GSnippingToolMainWindow()
    window.show()

    app.exec()


if __name__ == "__main__":
    main()