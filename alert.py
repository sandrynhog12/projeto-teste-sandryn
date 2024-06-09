#ALERTAR E PDIR INFORMAÇÃO NO PYAUTOGUI#

import pyautogui as pa
import time
import pyperclip

email = pa.prompt(text='- digite seu e-email: ', title='Dados do login: ')
senha = pa.prompt(text='- digite sua senha: ', title='Dados do login: ' )
pa.PAUSE = 0.5
pa.click(920,122,duration=1)
for i in range(1):
    pa.typewrite(f' Email:  {email}')
    pa.press('ENTER')
    pa.typewrite(f' Senha:  {senha}')
    pa.moveTo(960,346,duration=1)
    pa.leftClick(960,346,duration=0.1)