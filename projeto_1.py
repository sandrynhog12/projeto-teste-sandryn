import pyautogui as pa
import time
import pyperclip
import webbrowser as webb

def escrever(escrever):
    pyperclip.copy(escrever)
    pa.hotkey('Ctrl', 'V')

pa.PAUSE = 1.5
webb.open_new_tab('https://www.instagram.com/')
pa.sleep(2)
pa.moveTo(78,267,duration=1)
pa.leftClick(78,267,duration=0.5)
escrever('nike')
pa.press('enter')
pa.leftClick(236,265,duration=0.5)
pa.leftClick(484,608,duration=0.5)
pa.leftClick(793,675,duration=0.5)
escrever('Vini Malzadeza! ')
pa.press('ENTER')


