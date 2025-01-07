import threading

from js2py.base import false

import ScreenReader
import keyboard
import time
from collections import deque

import UI

def analyze_br():
    ScreenReader.capture_application_screenshot("War Thunder", "war_thunder_screenshot.png")
    list = ScreenReader.get_list_of_friendly_planes_from_screenshot("war_thunder_screenshot.png", (820,400,350,1200))
    dict = {
        "F-16C" : 13.7,
        "F-16A" : 12.7,
        "F-15A" : 13.0,
        "F-15C MSIP II" : 13.7,
        "F-14A Early" : 12.7,
        "F-20A" :12.7,
        "OF-14A IRIAF" :12.7,
        "Su-27" : 13.0,
        "Mig-29SMT" :13.3,
        "Su-33":13.0,
        "Su-34":13.3,
        "F-15C MSIP Il": 13.7,
        "F-14B": 13.0,
        "Mirage 4000": 13.0,
        "#AMig-296": 13.0,
        "#AMig-29G": 13.0,
        "#F-4F KWS LV": 13.0,
        "F-4S Phantom II" : 12.0,
        "F-4S Phantom Il": 12.0,
        "Kfir C1O": 13.0,
        "Kfir C10": 13.0,
        "Kfir C1o": 13.0,
        "F-15]": 13.0,
        "F-15J": 13.0
    }
    br = 0.0
    for plane in list:
        if plane not in dict:
            print(f"The plane: '{plane}' is not Cataloged")
        else:
            br= max(br,dict[plane])
    return br

def detect_if_in_game ():
    ScreenReader.capture_application_screenshot("War Thunder", "war_thunder_screenshot.png")
    return ScreenReader.is_matching_progress_bar("war_thunder_screenshot.png", "war_thunder_game_bar.png", (1490,135,840,70), .65)


def main():
    while UI.is_done:
        time.sleep(1)
        print("Debug: Waiting For UI To Finish")
    cur_game_br = 0.0
    boolean_list = deque(maxlen=7)
    UI.update_text("...")
    # Check if TAB is pressed
    while True:
        # Check if TAB is pressed

        boolean_list.appendleft(detect_if_in_game())
        print(f"Debug Info: \tIn a Match: {any(boolean_list)}\t Cur BR: {cur_game_br}")

        if cur_game_br == 0.0 and any(boolean_list):
            UI.update_text("Press Tab")
            if keyboard.is_pressed('tab'):
                UI.update_text("Processing...")
                cur_game_br= analyze_br()
                UI.update_text(f"BR {max(cur_game_br - 1, 1.0)} - {cur_game_br}")

        elif cur_game_br != 0.0 and not any(boolean_list):
            UI.update_text("")
            cur_game_br=0.0
            time.sleep(10)

        elif cur_game_br ==0.0 and not any(boolean_list):
            time.sleep(5)


thread = threading.Thread(target=main)
thread.start()
UI.create_window()