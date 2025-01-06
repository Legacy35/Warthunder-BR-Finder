import ScreenReader
import keyboard
# Example usage

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
    if br !=0.0:
        print(f"The BR for this lobby is {max(br-1,1.0)} - {br}")

# Check if TAB is pressed
while True:
    # Check if TAB is pressed
    if keyboard.is_pressed('tab'):
        if keyboard.is_pressed('f8'):
            analyze_br()
            while keyboard.is_pressed('tab'):
                continue

    # Check if ALT+F8 is pressed
    if keyboard.is_pressed('alt+f8'):
        print("ALT+F8 pressed. Exiting...")
        break