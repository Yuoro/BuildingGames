'''
Notes:
What we need:
- RGB Value (the colour value)

'''

from pyautogui import *
import pyautogui
import time
import keyboard
import random
import win32api, win32con

# Tile 1: X:  602 Y: 1150 RGB: (208, 109, 118)
# Tile 2: X:  769 Y: 1150 RGB: (200, 102, 118)
# Tile 3: X:  943 Y: 1150 RGB: (205, 106, 118)
# Tile 4: X: 1122 Y: 1150 RGB: (202, 104, 118)


def click(x,y):
    win32api.SetCursorPos((x, y))
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, 0, 0)
    time.sleep(0.1)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, 0, 0)


while keyboard.is_pressed('q') == False:
    if pyautogui.pixel(602, 1100)[0] == 0:
        click(602, 1100)
    if pyautogui.pixel(769, 1100)[0] == 0:
        click(769, 1100)
    if pyautogui.pixel(943, 1100)[0] == 0:
        click(943, 1100)
    if pyautogui.pixel(1122, 1100)[0] == 0:
        click(1122, 1100)


