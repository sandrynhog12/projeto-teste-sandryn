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


driver.get('https://cursoautomacao.netlify.app/')
sleep(3)
janela_inicial = driver.current_window_handle
print(f'janela incial{janela_inicial}')
driver.execute_script('window.scrollTo(0,750);')
sleep(5)
button_new_window = driver.find_element(By.XPATH,'//button[@onclick="abrirJanela()"]')
sleep(5)
button_new_window.click()
janelas = driver.window_handles

for janela in janelas:
    print(janela)
    if janela not in janela_inicial:
        driver.switch_to.window(janela)
        # sleep(5)
        campo_pesquisa = driver.find_element(By.XPATH,'//input[@class="form-control"]')
        sleep(3)
        campo_pesquisa.click()
        sleep(3)
        campo_pesquisa.send_keys('Automação em Python ')
        sleep(2)
        fazer_pesquisa = driver.find_element(By.ID,'fazer_pesquisa')
        sleep(5)
        fazer_pesquisa.click()
        sleep(5)
        driver.close()
driver.switch_to.window(janela_inicial)      
input('')
driver.close()