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


driver.get('https://www.facebook.com/')
sleep(3)
campo_email = driver.find_element(By.ID,'email')
sleep(2)
campo_email.send_keys('alessadro.jump.oliveira@gmail.com')
sleep(2)
campo_senha = driver.find_element(By.ID,'pass')
sleep(1)
campo_senha.send_keys('Euamodayane12@')
sleep(1)
botao_enviar = driver.find_element(By.XPATH,'//button[@name="login"]')
sleep(1)
botao_enviar.click()
sleep(5)
compartilhar = driver.find_element(By.XPATH,'//div[@class="xi81zsa x1lkfr7t xkjl1po x1mzt3pk xh8yej3 x13faqbe"]')
compartilhar.click()
sleep(2)

campo_status = driver.find_element(By.XPATH,'//p[@class="xdj266r x11i5rnm xat24cr x1mh8g0r x16tdsg8"]')
sleep(3)
campo_status.send_keys('Olá, estou utilizando o FaceBook! ')
sleep(3)
botao_puclicar = driver.find_element(By.XPATH,'//div[@class="x1n2onr6 x1ja2u2z x78zum5 x2lah0s xl56j7k x6s0dn4 xozqiw3 x1q0g3np xi112ho x17zwfj4 x585lrc x1403ito x972fbf xcfux6l x1qhh985 xm0m39n x9f619 xn6708d x1ye3gou xtvsq51 x1r1pt67"]')
sleep(2)
botao_puclicar.click()

input('')
driver.close()