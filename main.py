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
        "F-15J": 13.0,
        "A-1OA Late": 10.7,
        "A-10A Late": 10.7,
        "A-1OC": 11.7,
        "A-10C": 11.7,
        "A-1OA": 10.3,
        "A-10A":10.3,
        "J-7E": 11.3,
        "J-7D": 10.7,
        "JF-17":13.3,
        "J-8F": 13.0,
        "F-5E": 11.0,
        "F-SE": 11.0,
        "F-SC": 10.7,
        "F-5C": 10.7,
        "F-5A": 10.7,
        "F-SA": 10.7,
        "F-105D": 10.3,
        "A-7D": 10.3,
        "A-7E":10.7,
        "F-8E":10.7,
        "AJS37": 11.0,
        "Mig-21bis": 11.0,
        "OMig-21bis":11.0,
        "F-111A": 10.7,
        "F-111F": 11.7,
        "AV-8C": 9.7,
        "#F-104G":11.0,
        "MiG-21bis-SAU" :11.0,
        "Su-25K": 10.3,
        "Su-25": 10.3,
        "Su-25BM": 11.3,
        "Su-25T": 11.7,
        "FSU-2":10.3,
        "FBU-2": 10.3,
        "F-4C Phantom":10.3,
        "F-4C Phantom II":10.3,
        "F-4C Phantom Il":10.3,
        "F-4C Phantom ll": 10.3,
        "MiG-21MF": 10.7,
        "ZMiG-21MF":10.7,
        "Mig-21 \"Lazur-":11.0,
        "Mig-21 \"Lazur-.":11.0,
        "F-15E": 14.0,
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
                if cur_game_br ==0.0:
                    UI.update_text("Failed to Identify BR")
                else:
                    UI.update_text(f"BR {max(cur_game_br - 1, 1.0)} - {cur_game_br}")

        elif cur_game_br != 0.0 and not any(boolean_list):
            UI.update_text("")
            cur_game_br=0.0
            time.sleep(10)

        elif cur_game_br ==0.0 and not any(boolean_list):
            UI.update_text("")
            time.sleep(5)
#'JA3ZC', 'OF-104G', 'AJS37', 'A-1OA Late', 'J-7D', 'F-SE', 'F-SC', 'F-SC', 'Mig-21bis', 'A-10A', 'A-10A', 'F-SC', 'Buccaneer S.2B', 'F-SC', 'A-10A Late', 'A-10A'

thread = threading.Thread(target=main)
thread.start()
UI.create_window()