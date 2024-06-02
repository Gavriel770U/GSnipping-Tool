import pyautogui
from pynput import mouse, keyboard

class GSnippingTool(object):
    def __init__(self) -> None:
        self.__base_path: str = r'./'
        
        with mouse.Listener (
            on_click=self.__on_click,
        ) as listener:
            listener.join()
        
        with keyboard.GlobalHotKeys (
            {
                '<ctrl>+<alt>+f': self.__full_screenshot_callback,
                '<ctrl>+<alt>+i': self.__part_screenshot_callback,
            }
        ) as global_hot_keys:
            global_hot_keys.join()
        
        
    def __on_click(self, x, y, button, pressed):
        print('{0} at {1}'.format('Pressed' if pressed else 'Released',(x, y)))
        if not pressed:
            # Stop listener
            return False
        
    
    def __full_screenshot_callback(self) -> None:
        self.take_screenshot()
    
    
    def __part_screenshot_callback(self) -> None:
        # TODO: implement this
        print("Not implemented...")
    
    
    def take_screenshot(self, region: tuple = None) -> None:
        pyautogui.screenshot(imageFilename=self.__base_path+'my_screenshot.png')