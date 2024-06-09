import pyautogui as pa
import time
import pyperclip

pa.PAUSE = 2
pa.press('win')
pa.write('WhatsApp')
pa.press('ENTER')
pa.sleep(3)
pa.click(x=264, y=270)
pa.click(x=707, y=698)
pyperclip.copy(" Te amo, minha Nega ")
pa.hotkey('ctrl', 'v')
pa.press('ENTER')
pa.press('Esc')


#pa.sleep(4)
#print(pa.position())


