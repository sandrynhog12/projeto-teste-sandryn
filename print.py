import pyautogui as pa
import webbrowser as wb
import pyperclip
import time

def escrver_frase(escrever):
    pyperclip.copy(escrever)
    pa.hotkey('Ctrl', 'c')

pa.PAUSE =0.8

wb.open_new(' https://cursoautomacao.netlify.app/')
pa.moveTo(1094,436,duration=0.5)
pa.leftClick(1094,436,duration=0.5)
pa.scroll(-7000)
pa.moveTo(775,300,duration=0.5)
pa.leftClick(775,300)
pa.write('Alessandro')
pa.moveTo(761,330,duration=0.5)
pa.leftClick(761,330)
pa.sleep(1)
pa.moveTo(1185,166,duration=0.8)
pa.leftClick(1185,166)
pa.scroll(-3950)
pa.moveTo(837,414,duration=0.5)
pa.leftClick(837,414)
pa.moveTo(820,529,duration=0.5)
pa.leftClick(820,529)
pa.moveTo(839,646,duration=0.5)
pa.leftClick(839,646)

pa.sleep(30)


pa.alert('Você terminou, Parabéns!, digite um OK para concluir. ')
