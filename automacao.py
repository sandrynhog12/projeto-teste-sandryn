import pyautogui as pa
import time
import pyperclip

pa.PAUSE = 1
pa.press('win')
pa.write('chrome')
pa.press('ENTER')
pa.write('youtube.com')
pa.press('ENTER')
time.sleep(3)
pa.click(x=614, y=119)
pyperclip.copy("Naruto uzumaki")
pa.hotkey('ctrl', 'v')
pa.press('ENTER')
pa.click(x=519, y=486)
pa.sleep(10)
pa.press('f')

#pa.sleep(5)
#print(pa.position())

