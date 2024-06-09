import pyautogui as pa
import time 

pa.PAUSE = 1

pa.moveTo(592,306,duration=0.3)
pa.dragTo(1103,482,button='left', duration=1) # ARRASTA O ARQUIVO 
pa.moveTo(998,300,duration=0.2) # MOVE O MOUSE
pa.click(998,300) # CLICA NA REGIÃO
pa.press('esc') # PRESSIONA A TECLA 
pa.moveTo(990,316,duration=0.3)
pa.click(990,316)