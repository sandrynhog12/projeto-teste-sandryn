from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from time import sleep
import random

def iniciar_driver():
    chrome_options = Options()
    arguments = ['--lang=pt-BR', '--window-size=800,1000', '--incognito']
    for argument in arguments:
        chrome_options.add_argument(argument)

    chrome_options.add_experimental_option('prefs', {
        'download.prompt_for_download': False,
        'profile.default_content_setting_values.notifications': 2,
        'profile.default_content_setting_values.automatic_downloads': 1,

    })
    driver = webdriver.Chrome(service=ChromeService(
        ChromeDriverManager().install()), options=chrome_options)

    return driver


driver = iniciar_driver()

def digitar_naturalmente(text,elemento):
    for letra in text:
        elemento.send_keys(letra)
        sleep(random.randint(1,2)/30)

driver.get('https://cursoautomacao.netlify.app/desafios.html')
sleep(3)
driver.execute_script("window.scrollTo(0, 1150);")
sleep(2)
paragrafo = driver.find_element(By.ID,"campoparagrafo")
sleep(2)
texto = ''' CARTA PARA DEUS.

SENHOR, ULTIMAMENTE AS COISAS ESTÃO COMPLICADAS. ESTAMOS DESANIMADOS, POIS NADA PARECE DAR CERTO EM NOVSSAS VIDAS. ESTAMOS PRECISANDO DE UM EMPREGO, PORÉM NUNCA CHEGA ESSAS VAGAS. ESTAMOS PRECISANDO DE UMA REVIRAVOLTA EM NOSSAS FINANÇAS, MAS NADA ACONTECE. ESTAMOS PRECISANDO COMPRAR NOSSA CASA OU NOSSO AP, TODAVIA, NADA ACONTECE.
PORTANTO, PRECISAMOS DE UM AGIR DO SENHOR EM NOSSAS VIDAS, PORQUE A CADA DIA QUE PASSA, FICA MAIS DIFÍCIL. EU SEI QUE O SENHOR PODE FAZER AS MESMAS COISAS QUE FEZ COM OS TEUS SERVOS NO PASSADO, COMO: MOISÉS, ELIAS, ABRAÃO, ISAQUE, JACÓ, DENTRE OUTROS, LOGO, PODE FAZER EM NOSSAS VIDAS TAMBÉM, PORQUE ÉS O MEMSO DE ANTIGAMENTE, PORQUANTO NAÕ MUDA A SUA NATUREZA DE AMOR E CUIDADO PARA COM AQUELES QUE TE AMAM. VENHO ATRAVÉS DESSA CARTA PEDIR A SUA AJUDA, PEDIR QUE O SENHOR ME ABENÇOE, ABENÇÕE A MINHA CASA, MINHA SAÚDE, MINHA ESPOSA E A SAÚDE DELA E QUE OUÇA NOSSAS ORAÇÕES. ESTOU NO AGUARDO DE UMA RESPOSTA OU UMA PROVIDEÊNCIA DA SUA PARTE. TE AMO JESUS! '''

sleep(2)
digitar_naturalmente(texto,paragrafo)
sleep(2)

validar = driver.find_element(By.CLASS_NAME,'btn.btn-success')
validar.click()

input('')
driver.close()