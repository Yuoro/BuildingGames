from pyautogui import *
import pyautogui
import time
import keyboard
import random
import win32api, win32con

while 1:
    if pyautogui.locateOnScreen('stickman.png', region=(75,250,345, 525), grayscale=True, confidence=0.8) is not None:
        print('I can see it')
        time.sleep(0.5)
    else:
        print("I can't see it")
        time.sleep(0.5)

