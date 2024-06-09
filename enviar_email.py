import pyautogui as pa
import time
import pyperclip
import webbrowser as webb




def escrever (digitar):
    pyperclip.copy(digitar)
    pa.hotkey('ctrl', 'V')



for i in range(30):

    
    pa.PAUSE = 0.3


    # webb.open('https://mail.google.com/mail/u/0/?tab=rm&ogbl#inbox')

    pa.moveTo(30,181,duration=1)

    pa.leftClick(30,181,duration=1)
  
    pa.leftClick(932,302,duration=1)
    escrever('recrutamentopcd@brasfort.com.br')
    pa.press('tab')
    escrever('Vaga Para Brigadista ou qualquer outra vaga relacionada ao meu perfil. ')
    pa.press('tab')
    escrever('Olá, me chamo Alessandro! Estou em busca de uma oportunidade. ')
   
    pa.leftClick(963,684,duration=1)
  
    pa.leftClick(97,178,duration=1)
   
    pa.doubleClick(283,499,duration=1)
 
    pa.leftClick(857,687,duration=1)