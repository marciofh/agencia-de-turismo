from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time


from selenium import webdriver
from selenium.webdriver.firefox.options import Options
options = Options()
#options.headless = True
driver = webdriver.Firefox(options=options)

url = "https://www.voeazul.com.br/"
driver.get(url)
driver.maximize_window()
time.sleep(2)

#INSERINDO DADOS
field = driver.find_element(By.NAME, "origin1")
time.sleep(1)
field.send_keys("São Paulo", Keys.ENTER)

field2 = driver.find_element(By.NAME, "destination1")
time.sleep(1)
field2.send_keys("Rio de Janeiro", Keys.ENTER)

field3 = driver.find_element(By.NAME, "departure1")
time.sleep(1)
field3.send_keys("27/06/2022")

field4 = driver.find_element(By.NAME, "arrival")
time.sleep(1)
field4.send_keys("29/06/2022")

passageiro = driver.find_element(By.ID, "incrementAdults")
time.sleep(1)
for i in range(3-1):
    passageiro.click()
    time.sleep(1)

submit = driver.find_element(By.ID, "searchTicketsButton")
time.sleep(1)
submit.click()
time.sleep(10)