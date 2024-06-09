import pyautogui as pa
import time
import pyperclip

pa.PAUSE = 2
pa.press('Win')
pa.write('Excel')
pa.press('ENTER')
pa.click(x=58, y=270, clicks= 2)
pa.moveTo(x=281, y=212, duration= 2)
pa.click(x=298, y=200, clicks= 2)
pa.click(x=57, y=308)
pa.write('Alessandro De Jesus')
pa.click(x=85, y=291, clicks= 2)
pa.moveTo(x=244, y=119, duration= 1)
pa.click(x=244, y=119)
pa.click(x=329, y=124)