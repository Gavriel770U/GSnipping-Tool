from pynput import keyboard

ESC_COMBINATION: dict = {keyboard.Key.esc}
CMD_COMBINATION: dict = {keyboard.Key.cmd}
LALT_TAB_COMBINATION: dict = {keyboard.Key.alt_l, keyboard.Key.tab}
CMD_TAB_COMBINATION: dict = {keyboard.Key.cmd, keyboard.Key.tab}

FULL_SCREEN_SNIP_ACTION: str = 'full_screen_snip_action'
RECTANGLE_SNIP_ACTION: str = 'rectangle_snip_action'

NO_DELAY_ACTION: str = 'no_delay_action'
ONE_SECOND_DELAY_ACTION: str = 'one_second_delay_action'
TWO_SECONDS_DELAY_ACTION: str = 'two_seconds_delay_action'
THREE_SECONDS_DELAY_ACTION: str = 'three_seconds_delay_action'
FOUR_SECONDS_DELAY_ACTION: str = 'four_seconds_delay_action'
FIVE_SECONDS_DELAY_ACTION: str = 'five_seconds_delay_action'
