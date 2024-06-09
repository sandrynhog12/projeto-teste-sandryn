import pyautogui as pa
import time
import webbrowser as wb
import pyperclip

def escrever(escrever):
    pyperclip.copy(escrever)
    pa.hotkey('ctrl', 'V')


 

telefones = [5561992624888]

for telefone in telefones:
    pa.PAUSE =1

    wb.open_new_tab(f'https://api.whatsapp.com/send?phone={telefone}')
    pa.leftClick(725,328,duration=5)
    pa.leftClick(641,696)
    escrever('Estou descendo lá na sua mãe. Já Já levo a comida do meu bem! ')
    pa.press('ENTER')
    pa.sleep(3000)