import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from whatsapp_api import WhatsApp
from time import sleep
import urllib


navegador = webdriver.Chrome()
navegador.get('https://web.whatsapp.com')



#Espera aparecer o elemento que tem o is 'side'
while len(navegador.find_elements_by_id('side')) < 1:
	sleep(1)


contatos_df = pd.read_excel(r'./Enviar.xlsx')



for i, mensagem in enumerate(contatos_df['Mensagem']):
	pessoa = contatos_df.loc[i, "Pessoa"]
	numero = contatos_df.loc[i, "Numero"]
	texto = urllib.parse.quote(f'Olá {pessoa}, {mensagem}')

	link = f'https://web.whatsapp.com/send?phone={numero}&text={texto}'

	navegador.get(link)

	navegador.find_element_by_xpath('//*[@id="main"]/footer/div[1]/div[2]/div/div[1]/div/div[2]').send_keys(Keys.ENTER)

	sleep(10)

	while len(navegador.find_elements_by_id('side')) < 1:
		sleep(1)


