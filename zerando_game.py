
# quais são os passos manuais que devo transformar em código
import pyautogui
import keyboard
import win32api
import win32con
from time import sleep

pyautogui.click(530,516, duration=1)


def click(x, y):
    win32api.SetCursorPos((x, y))
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, 0, 0)
    sleep(0.01)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, 0, 0)


while keyboard.is_pressed('1') == False:
    if pyautogui.pixelMatchesColor(531,354, (0, 0, 0)):
        click(531,354)
    if pyautogui.pixelMatchesColor(619,358, (0, 0, 0)):
        click(619,358)
    if pyautogui.pixelMatchesColor(692,351, (0, 0, 0)):
        click(692,351)
    if pyautogui.pixelMatchesColor(756,346, (0, 0, 0)):
        click(756,346)