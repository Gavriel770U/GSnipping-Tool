from pynput import keyboard

COMBINATIONS = [
    {
        keyboard.Key.esc,
    },
    
    {
        keyboard.Key.cmd,
        keyboard.Key.tab,
    },
]

current = set()

def execute1() -> None:
    print("Detected hotkey #1")

def execute2() -> None:
    print("Detected hotkey #2")

def on_press(key) -> None:
    if any([key in combination for combination in COMBINATIONS]):
        current.add(key)
        if any(all(k in current for k in combination) for combination in COMBINATIONS):
            if set({keyboard.Key.esc}) == current:
                execute1()
            else:
                execute2()
            
def on_release(key) -> None:
    if any([key in combination for combination in COMBINATIONS]):
        current.remove(key)
        

with keyboard.Listener(on_press=on_press, on_release=on_release) as listener:
    listener.join()