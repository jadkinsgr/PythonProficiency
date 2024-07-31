import pyautogui
import time

while True:
    pyautogui.move(100, 100)
    time.sleep(1)
    pyautogui.move(-100, -100)
    time.sleep(1)
    pyautogui.click()
    time.sleep(20)
