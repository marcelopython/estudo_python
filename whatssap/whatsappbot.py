from selenium import webdriver
import time
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys
#Navegar ate o whatsapp web
driver = webdriver.Chrome(ChromeDriverManager().install())
driver.get('https://web.whatsapp.com/')
time.sleep(5)

#definir contatos e grupos e mensagem a ser enviadas
contatos = ['Deir', 'Marcos Irm', 'jao paulo', 'Keven', 'Lorrane', 'Joaby']
mensagem = 'Teste do envio de mensagem'
#buscar contatos/grupos # copyable-text selectable-text
def buscar_contato(contato):
    campo_pesquisa = driver.find_element_by_xpath('//div[contains(@class, "copyable-text selectable-text")]')
    campo_pesquisa.click()
    campo_pesquisa.send_keys(contato)
    campo_pesquisa.send_keys(Keys.ENTER)

def enviar_mensagem(mensagem):
    campo_message = driver.find_elements_by_xpath('//div[contains(@class, "copyable-text selectable-text")]')
    campo_message[1].click()
    campo_message[1].send_keys(mensagem)
    campo_message[1].send_keys(Keys.ENTER)

for contato in contatos:
    buscar_contato(contato)
    # Enviar mensagens para o contato/grupo
    enviar_mensagem(mensagem)

#campo de mensagem privada copyable-text selectable-text


