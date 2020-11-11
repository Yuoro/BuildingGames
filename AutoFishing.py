from pyautogui import *
import pyautogui
import time
import keyboard
import random
import win32api, win32con

'''
Input: Left click
It will then store the position of that left click
'''


def sim_left_click(x,y):
    #win32api.SetCursorPos(x, y)
    pyautogui.moveTo(x, y)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, 0, 0)
    time.sleep(0.5)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, 0, 0)



while keyboard.is_pressed("q") is False:
        if pyautogui.locateOnScreen('fatefishing.png', region=(450,125,100, 150), confidence=0.85) is not None:
            sim_left_click(475, 870)
            time.sleep(4)





'''
        if pyautogui.locateOnScreen('ok.png', region=(825,700,275, 100), confidence=0.85) is not None:
            sim_left_click(885, 750)
            time.sleep(2)
'''

'''
while keyboard.is_pressed("q") is False:
    if pyautogui.locateOnScreen('fatefishing.png', region=(225,100,600, 250), confidence=0.8) is not None:
        click(600, 870)
        time.sleep(0.5)
'''

'''
def click(x,y):
    win32api.SetCursorPos((x, y))
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, 0, 0)
    time.sleep(0.5)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, 0, 0)
'''



