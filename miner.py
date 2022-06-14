# auto miner script - holds w and left click until
# we reach a certain point
#
#
# written by saiini
#
import pyautogui, sys
import pydirectinput
import time
import threading

#
# threshold
#
clickiterationConstant = 13
clickIterationRange = range(clickiterationConstant)
def clickThread():
    for i in clickIterationRange:
        #
        # iterate until we reached the constant value
        #
        print(f"click iteration: {i}")
        pyautogui.mouseDown();

def keyThread():
    start = time.time()
    pydirectinput.keyDown('shift')
    while time.time() - start < clickiterationConstant:
        #
        # iterate until we reached the constant value
        #
        pydirectinput.keyDown('w')
        pydirectinput.keyUp('w')
        


        

if __name__ == '__main__':
    print("starting click and walk thread")
    time.sleep(5)
    print("Holding for 5 seconds, make sure your game window is open")
    threading.Thread(target = clickThread).start()
    threading.Thread(target = keyThread).start()
