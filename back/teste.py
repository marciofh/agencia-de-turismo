from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
from bs4 import BeautifulSoup
import pandas as pd

#CONFIGURAÇÕES DO DRIVER
options = Options()
options.headless = True
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
input_cidade('edit-fieldset-origin', 'São Paulo') #ORIGEM
input_cidade('edit-fieldset-destiny', 'Salvador') #DESTINO

#INPUT PASSAGEIRO
div_passageiro = driver.find_element(By.ID, "edit-fieldset-passengers")
time.sleep(1)
div_passageiro.click()
passageiro = driver.find_element(By.NAME, "add_pass")
time.sleep(1)
for i in range(3-1): #PASSAGEIRO
    passageiro.click()
    time.sleep(1)

submit_passageiro = driver.find_element(By.ID, "passengers-apply")
time.sleep(1)
submit_passageiro.click()

#INPUT DATA
input_data("edit-departure-date", '01072022') #DATA IDA
input_data("edit-back-date", '03072022') #DATA VOLTA

#SUBMIT
bnt_submit = driver.find_element(By.ID, "search-flights")
time.sleep(1)
bnt_submit.click()
time.sleep(10)

#PEGANDO HTML DA RESPOSTA
form = driver.find_element(By.XPATH, "//section[@class='ng-tns-c148-0 ng-star-inserted']")
time.sleep(1)
html_text = form.get_attribute('outerHTML')
soup = BeautifulSoup(html_text, 'html.parser')

list = []
for span in soup.find_all(class_='a-desc__value'):
    list.append(span.get_text())

#TRATANDO DADO
df = pd.DataFrame(list)
df = df.rename(columns = {0 : 'valores'})
passagens = pd.DataFrame()
tamanho = int(len(df) / 5)

for i in range(tamanho):
    voo = df.iloc[:5]
    passagens['coluna ' + str(i)] = voo
    df = df.drop(df.index[:5])
    df.reset_index(inplace = True, drop = True)

passagens = passagens.transpose()
passagens.reset_index(inplace = True, drop = True)
passagens = passagens.rename(columns={0 : 'origem'})
passagens = passagens.rename(columns={1 : 'destino'})
passagens = passagens.rename(columns={2 : 'duracao'})
passagens = passagens.rename(columns={3 : 'conexao'})
passagens = passagens.rename(columns={4 : 'preco'})
passagens['duracao'] = passagens['duracao'].replace(' ,', '', regex = True)

print(passagens)



driver.quit()