import pyautogui, sys
import pydirectinput
import time
import threading
#
# Author: sa111n111
#
def clickThread():
    for i in range(1000000):
        print(f"click iteration: {i}")
        pyautogui.mouseDown();
        pyautogui.mouseUp();
        time.sleep(4)

if __name__ == '__main__':
    print("starting click thread")
    
    time.sleep(5)
    threading.Thread(target = clickThread).start()

    print("Threads started succesfully. Happy XP Grinding! =)")
