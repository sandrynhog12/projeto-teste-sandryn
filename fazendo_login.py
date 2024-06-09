from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from time import sleep


def iniciar_driver():
    chrome_options = Options()
    arguments = ['--lang=pt-BR', '--window-size=800,600', '--incognito']
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
sleep(5)
botao_login = driver.find_element(By.LINK_TEXT,'Login')
sleep(1)
botao_login.click()
sleep(1)
botao_email = driver.find_element(By.ID,'email')
sleep(1)
botao_email.click()
sleep(1)
botao_email.send_keys('sandrynhog12@gmail.com')
sleep(1)
campo_senha = driver.find_element(By.ID,'senha')
sleep(1)
campo_senha.click()
sleep(1)
campo_senha.send_keys('Euamodayane12@')
sleep(1)
campo_enviar = driver.find_element(By.CLASS_NAME,'btn.btn-primary')
sleep(1)
campo_enviar.click()

input('Seu programa rodou perfeitamente! ')
driver.close()
