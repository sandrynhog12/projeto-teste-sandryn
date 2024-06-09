from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from time import sleep

def iniciar_driver():
    chrome_options = Options()
    arguments = ['--lang=pt-BR', '--window-size=900,1200', '--incognito']
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


driver.get('https://cursoautomacao.netlify.app/desafios')

botao_desafios = driver.find_element(By.ID,"dadosusuario")
sleep(3)
driver.execute_script("window.scrollTo(0, 380);")
sleep(2)
botao_desafios.send_keys('Alessandro De Jesus Oliveira ')
sleep(1)
botao_desafios.click()
sleep(1)
clique_aqui = driver.find_element(By.ID,'desafio2')
sleep(1)
clique_aqui.click()
sleep(5)

escondido = driver.find_element(By.ID,'escondido')
sleep(2)
escondido.click()
sleep(2)
escondido.send_keys('Alessandro De Jesus Oliviera')
sleep(2)
valida = driver.find_element(By.ID,'validarDesafio2')
sleep(2)
valida.click()

driver.execute_script("window.scrollTo(0, 1000);")
sleep(1)
botao_maveric = driver.find_element(By.ID,'conversivelcheckbox')
sleep(1)
botao_maveric.click()
sleep(1)
botao_moto = driver.find_element(By.ID,'motocheckbox')
sleep(1)
botao_moto.click()
sleep(1)
botao_of_road = driver.find_element(By.ID,'offroadcheckbox')
sleep(1)
botao_of_road.click()
sleep(5)

campo_paragrafo = driver.find_element(By.ID,'campoparagrafo')
sleep(2)
campo_paragrafo.click()
sleep(1)
campo_paragrafo.send_keys('Olá, me chamo Alessandro De Jesus Oliveira. Estou atrás de uma vaga! ')

validar_2 = driver.find_element(By.CLASS_NAME,'btn.btn-success')
sleep(1)
validar_2.click()
sleep(5)


input('')
driver.close()