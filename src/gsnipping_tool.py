import pyautogui
from pynput import mouse

class GSnippingTool(object):
    def __init__(self) -> None:
        self.__base_path: str = r'./'
        
        with mouse.Listener (
            on_click=self.__on_click,
        ) as listener:
            listener.join()
        
    def __on_click(self,x, y, button, pressed):
        print('{0} at {1}'.format('Pressed' if pressed else 'Released',(x, y)))
        if not pressed:
            # Stop listener
            return False
    
    def take_screenshot(self, region: tuple = None) -> None:
        pyautogui.screenshot(imageFilename=self.__base_path+'my_screenshot.png')