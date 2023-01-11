from rich.console import Console
from rich.text import Text
from lib import aimer
from lib import helpers
from lib import keycodes
from lib.bones import bones
import ctypes
import random, threading, time

console = Console()

#### CHANGE OPTIONS HERE ####

# Field of View
# Alter this between 0.1 and 3.0 for best results. 0.1 is very narrow, while larger numbers allow
# for more soldiers to be targeted
fov = 1.5

# Distance Limit
# Example, set to 100 to limit locking onto soldiers further than 100 meters away.
distance_limit = 100 # can also be: None

# Trigger Button
# Grab your preferred button from lib/keycodes.py
trigger = keycodes.XBUTTON2

# If set to True you will automatically crouch and uncrouch while shooting others.
# According to my experience this will make you be less shot by others.
dodge_Mode = False

# Your key to crouch. Use a string here instead of a keycode.
crouch_Key = "ctrl"

# Keybind to enable or disable Dodge Mode
toggle_dodge_Mode = keycodes.PAGEUP

# Keep Target will continue to aim at your target, even if they are occluded.
toggle_keep_target = keycodes.NUMPAD7

# If set to True your weapon will automatically shoot after finding a target
autoshoot = True

# Toggle autoshoot. Use this if you are using a sniper or a small magazine.
toggle_autoshoot = keycodes.DELETE

# If set to True your weapon will automatically scope as soon as you lock onto a target
autoscope = True

# Press this button to switch between normal aimbot and hunt
hunt_Toggle = keycodes.NUMPAD5

# Press this and you have to input a name into the console to hunt. You don't need to write the exact name the program will try to find the name with the most matches.
hunt_Target_Switch = keycodes.NUMPAD8

# Aim Location Options
# Aim Location Switching (default is the first one listed)
# Check available bones in lib/bones.py
aim_locations = [bones['Head'], bones['Spine'], bones['Neck'], bones['Hips']]

# Key to switch aim location (set to None to disable)
aim_switch = keycodes.PAGEDOWN
#aim_switch = None

# Normally, you won't need to change this
# This will attempt to gather your primary screen size. If you have issues or use
# a windowed version of BFV, you'll need to set this yourself, which probably comes with its own issues
screensize = ctypes.windll.user32.GetSystemMetrics(0), ctypes.windll.user32.GetSystemMetrics(1)
# or
#screensize = (1280, 960)

collection = [fov, distance_limit, trigger, autoshoot, autoscope, aim_locations, aim_switch, screensize, hunt_Toggle, hunt_Target_Switch, dodge_Mode, crouch_Key, toggle_autoshoot, toggle_dodge_Mode, toggle_keep_target]

#### END OF CHANGE OPTIONS ####

if __name__ == "__main__":
    try:
        if fov < 0.1 or fov > 3.0:  # you can delete this if you know what you're doing
            raise Exception("Check your fov settings.")
            
        if distance_limit is not None and distance_limit <= 0:
            raise Exception("Check your distance_limit settings")

        if not helpers.is_admin():
            raise Exception("[X] Error: This must be run with admin privileges")

        if not helpers.is_python3():
            raise Exception("[X] Error: This script requires Python 3")

        arch = helpers.get_python_arch()
        if arch != 64:
            raise Exception("[X] Error: This version of Python is not 64-bit")

    except Exception as e:
        console.print(e, style="red")
        exit(1)

aimer = aimer.Aimer(collection)
console.print(Text("[!] Using screensize: %s x %s" % screensize, style="bright_black"))
aimer.start()
