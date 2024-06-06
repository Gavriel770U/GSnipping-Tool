import pyautogui

class GSnippingToolScreenShoter:
    def __init__(self) -> None:
        self.__base_path: str = r'./'
    
    def take_screenshot(self, region: tuple = None) -> None:
        pyautogui.screenshot(imageFilename=self.__base_path+'my_screenshot.png')