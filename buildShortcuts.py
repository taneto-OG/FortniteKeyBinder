import os
import time
import autopy
import pyautogui
import keyboard as k
from pynput.keyboard import Key, Controller

courrentPressed = "none"
lastClick = "none"

def exec(_courrentPressed):
    if (_courrentPressed != lastClick):
        if (_courrentPressed != "none"):
            print (_courrentPressed)
            keyboard = Controller()
            keyboard.press(_courrentPressed)
            keyboard.release(_courrentPressed)
            return (True)
    return (False)

while True:
    try:
        
        if courrentPressed == "p":
            courrentPressed = "none"
        if courrentPressed == ".":
            courrentPressed = "none"
        if courrentPressed == ",":
            courrentPressed = "p"
        if courrentPressed == "c":
            courrentPressed = "."
        if k.is_pressed("q"):
            courrentPressed = "c"
        else:
            if k.is_pressed("alt"):
                courrentPressed = ","
        if (exec(courrentPressed)):
            lastClick = courrentPressed
    except:
        print ("e")
