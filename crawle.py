from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
from datetime import datetime
from bs4 import BeautifulSoup
import pandas as pd

class Crawler:
    #CONFIGURAÇÕES DO DRIVER
    def __init__(self):
        self.URL = 'https://www.voegol.com.br'
        options = Options()
        #options.headless = True
        self.driver = webdriver.Firefox(options = options)
        self.driver.maximize_window()
    
    #FUNÇÃO CIDADE
    def input_cidade(self, id, cidade):
        div = self.driver.find_element(By.ID, id)
        time.sleep(1)
        div.click()
        field = self.driver.find_element(By.XPATH, "//input[@class='select2-search__field focus']")
        time.sleep(1)
        field.send_keys(cidade, Keys.ENTER)
    
    #FUNÇÃO DATA
    def input_data(self, id, data):
        print(data)
        data = datetime.strptime(data, "%Y-%m-%d").date()
        new_data = data.strftime( '%d/%m/%Y' )
        new_data = str(new_data)
        new_data = new_data.replace('/','')

        print(type(new_data))
        
        field = self.driver.find_element(By.ID, id)
        time.sleep(1)
        field.send_keys(data, Keys.ENTER)

    #TRATANDO DADOS
    def get_tabela(self, html_text):
        soup = BeautifulSoup(html_text, 'html.parser')
        lista = []

        for span in soup.find_all(class_= 'a-desc__value'):
            lista.append(span.get_text())
        df = pd.DataFrame(lista)
        df = df.rename(columns = {0 : 'valores'})
        passagens = pd.DataFrame()
        qtde = int(len(df) / 5)

        for i in range(qtde):
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

        return passagens
    
    #INPUT DADOS
    def send_dados(self, origem, destino, passageiros, data_ida, data_volta):
        self.driver.get(self.URL)
        time.sleep(2)
        #COOKIES
        cookies = self.driver.find_element(By.ID, "onetrust-accept-btn-handler")
        time.sleep(1)
        cookies.click()

        #CIDADE
        self.input_cidade('edit-fieldset-origin', origem) #ORIGEM
        self.input_cidade('edit-fieldset-destiny', destino) #DESTINO      

        #INPUT PASSAGEIRO

        div_passageiro = self.driver.find_element(By.ID, "edit-fieldset-passengers")
        time.sleep(1)
        div_passageiro.click()
        passageiro = self.driver.find_element(By.NAME, "add_pass")
        time.sleep(1)
        for i in range(int(passageiros) - 1): #PASSAGEIRO
            passageiro.click()
            time.sleep(1)

        submit_passageiro = self.driver.find_element(By.ID, "passengers-apply")
        time.sleep(1)
        submit_passageiro.click()

        #INPUT DATA
        self.input_data("edit-departure-date", data_ida) #DATA IDA
        self.input_data("edit-back-date", data_volta) #DATA VOLTA

        #SUBMIT IDA
        submit_ida = self.driver.find_element(By.ID, "search-flights")
        time.sleep(1)
        submit_ida.click()
        time.sleep(10)

        #PEGANDO PASSAGENS IDA
        section_ida = self.driver.find_element(By.XPATH, "//section[@class='ng-tns-c148-0 ng-star-inserted']")
        time.sleep(1)
        section_ida = section_ida.get_attribute('outerHTML')

        #SUBMIT VOLTA
        div_pass = self.driver.find_element(By.XPATH, "//div[@class='m-bar-product m-bar-product--border-bottom']")
        time.sleep(1)
        div_pass.click()
        submit_volta = self.driver.find_element(By.XPATH, "//button[@class='m-button m-button--isEnabled']")
        time.sleep(1)
        submit_volta.click()
        time.sleep(10)

        #PEGANDO PASSAGENS VOLTA
        section_volta = self.driver.find_element(By.XPATH, "//section[@class='ng-tns-c148-0 ng-star-inserted']")
        time.sleep(1)
        section_volta = section_volta.get_attribute('outerHTML')
        
        section = [section_ida, section_volta]
        return section

    #RETORNANDO DADOS
    def get_dados(self, sections):
        for section in sections:
            print(self.get_tabela(section))