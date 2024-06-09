from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from time import sleep
import random
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.keys import Keys #USAR BOTÕES DO TECLADO
def iniciar_driver():
    chrome_options = Options()
    arguments = ['--lang=pt-BR', '--window-size=1000,700', '--incognito']
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


driver.get('https://cursoautomacao.netlify.app/desafios.html')
sleep(3)
janela_inicial = driver.current_window_handle
print(f'janela incial{janela_inicial}')
driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
sleep(4)
open_window = driver.find_element(By.XPATH,'//button[text()="Abrir nova janela"]')
open_window.click()
janelas = driver.window_handles
for janela in janelas:
    print(janela)
    if janela not in janela_inicial:
        driver.switch_to.window(janela)
        campo_escrever = driver.find_element(By.ID,'opiniao_sobre_curso')
        campo_escrever.click()
        sleep(2)
        campo_escrever.send_keys('Meu nome é Alessandro e estou automatizando! ')
        sleep(3)
        button_enviar = driver.find_element(By.ID,'fazer_pesquisa')
        button_enviar.click()
        sleep(3)
        driver.close
driver.switch_to.window(janela_inicial)
digitar_texto2 = driver.find_element(By.ID,'campo_desafio7')
digitar_texto2.click()
sleep(2)
digitar_texto2.send_keys('Alessandro está Automatizando! ')
input('')
driver.close