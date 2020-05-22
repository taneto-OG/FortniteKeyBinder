import os
import time
import autopy
import pyautogui
import keyboard as k
from pynput.keyboard import Key, Controller

def exec(kp):
    print (kp)
    if kp != 'none':
        keyboard = Controller()
        keyboard.press(kp)
        keyboard.release(kp)

def invert(boolx):
    if (boolx):
        return (False)
    else:
        return (True)

kp = 'none'
switch = False
while True:
    try:
        if k.is_pressed('q'):
            kp = 'c'
        else:
            if k.is_pressed('alt'):
                kp = ','
            else:
                if kp == 'p':
                    kp = 'none'
                if kp == '.':
                    kp = 'none'
                if kp == ',':
                    kp = 'p'
                if kp == 'c':
                    kp = '.'

        print('-------------------')
        exec(kp)
        print('-------------------')
        os.system('cls')
        time.sleep(0.01)

    except:
        print('break')
        break
