from gsnipping_tool_capture import GSnippingToolCapture


class GSnippingToolScreenShoter:
    def __init__(self, main_window) -> None:
        self.__base_path: str = r'./'
        self.__main_window = main_window
    
    
    def take_screenshot(self) -> None:
        capture = GSnippingToolCapture()
        capture.destroyed.connect(self.__main_window.show)
        capture.show()
        print('Captured...')