from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from time import sleep

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
driver.execute_script("window.scrollTo(0, 200);")
sleep(1)
campo_usuario = driver.find_element(By.ID,'dadosusuario')
sleep(1)
campo_usuario.click()
sleep(1)
campo_usuario.send_keys('Alessandro De Jesus')
sleep(1)
campo_enviar = driver.find_element(By.ID,'desafio2')
sleep(1)
campo_enviar.click()
sleep(1)
campo_nome2 = driver.find_element(By.ID,'escondido')
sleep(1)
campo_nome2.click
sleep(1)
driver.execute_script("window.scrollTo(0, 300);")
sleep(1)
campo_nome2.send_keys('Alessandro De JEsus')
sleep(1)
validar = driver.find_element(By.ID,'validarDesafio2')
sleep(1)
validar.click()
sleep(5)

driver.execute_script("window.scrollTo(0, 900);")

chackbox_1 = driver.find_element(By.ID,'conversivelcheckbox')
chackbox_2 = driver.find_element(By.ID,'motocheckbox')
chackbox_3 = driver.find_element(By.ID,'offroadcheckbox')
sleep(1)
chackbox_1.click()
sleep(1)
chackbox_2.click()
sleep(1)
chackbox_3.click()

input('')
driver.close()
