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
# Rolar até o fim da página
driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
sleep(6)
# Rolar até o topo da página
driver.execute_script("window.scrollTo(0, document.body.scrollTop)")
sleep(6)
# Rolar X quantidade em pixels(descer)
driver.execute_script("window.scrollTo(0, 2500);")
sleep(6)
# Rolar X quantidade em pixels(subir)
driver.execute_script("window.scrollTo(0, -2500);")

input('')
driver.close()