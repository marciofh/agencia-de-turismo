from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
from bs4 import BeautifulSoup

#CONFIGURAÇÕES DO DRIVER
options = Options()
#options.headless = True
driver = webdriver.Firefox(options=options)
url = "https://www.voegol.com.br"
driver.get(url)
driver.maximize_window()
time.sleep(2)

def input_cidade(id,cidade):
    div = driver.find_element(By.ID, id)
    time.sleep(1)
    div.click()
    field = driver.find_element(By.XPATH, "//input[@class='select2-search__field focus']")
    time.sleep(1)
    field.send_keys(cidade, Keys.ENTER)

def input_data(id, data):
    field = driver.find_element(By.ID, id)
    time.sleep(1)
    field.send_keys(data, Keys.ENTER)

#CONFIRMANDO COOKIES
cookies = driver.find_element(By.ID, "onetrust-accept-btn-handler")
time.sleep(1)
cookies.click()

#INPUT CIDADE
input_cidade('edit-fieldset-origin', 'Rio de Janeiro')
input_cidade('edit-fieldset-destiny', 'Belo Horizonte')

#INPUT PASSAGEIRO
div_passageiro = driver.find_element(By.ID, "edit-fieldset-passengers")
time.sleep(1)
div_passageiro.click()
passageiro = driver.find_element(By.NAME, "add_pass")
time.sleep(1)
for i in range(3-1):
    passageiro.click()
    time.sleep(1)

submit_passageiro = driver.find_element(By.ID, "passengers-apply")
time.sleep(1)
submit_passageiro.click()

#INPUT DATA
input_data("edit-departure-date", '01072022')
input_data("edit-back-date", '03072022')

#SUBMIT
bnt_submit = driver.find_element(By.ID, "search-flights")
time.sleep(1)
bnt_submit.click()
time.sleep(10)

#PEGANDO HTML DA RESPOSTA
div = driver.find_element(By.XPATH, "//form")
time.sleep(1)
html = div.get_attribute('outerHTML')
soup = BeautifulSoup(html, 'html.parser')


voo = soup.find_all(class_='m-bar-product m-bar-product--border-bottom')
dados = voo.find_all(class_='a-desc__value')

print(dados)
# origem = voo[0].contents
# destino = voo[1].contents
# duração = voo[2].contents
# conexao = voo[3].contents
# preco = voo[4].contents

# print('Origem: ' + origem[0])
# print('Destino: ' + destino[0])
# print('Duração: ' + duração[0])
# print('Conexão: ' + conexao[0])
# print('Preço: ' + preco[2])