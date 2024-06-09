from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from time import sleep
import random
from selenium.webdriver.support.select import Select

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


driver.get('https://cursoautomacao.netlify.app/desafios.html')
sleep(3)
driver.execute_script('window.scrollTo(0,2400);')
sleep(5)

selecionar_paises = driver.find_element(By.XPATH,"//select[@id='paisesselect']")
option = Select(selecionar_paises)
sleep(1)
#index
option.select_by_index(1)
sleep(3)
#value
option.select_by_value('estadosunidos')
sleep(3)
#TEXTO DE EXIBIÇÃO
option.select_by_visible_text('Canada')
input('')

driver.close()
