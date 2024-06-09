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


driver.get('https://cursoautomacao.netlify.app/')

botao_mec = driver.find_element(By.ID,'MacRadioButton')
sleep(1)
botao_mec.click()
if botao_mec.is_selected() == True:
   print('O botão está selecionado! ')
   sleep(1)

# sleep(1)
# radios = driver.find_elements(By.XPATH,"//input[@type='radio']")
# sleep(1)
# radios[1].click()
# sleep(1)
# radios[0].click()
# sleep(1)
# radios[2].click()

input('')
driver.close()