from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.select import Select

servico = Service(ChromeDriverManager().install())
navegador = webdriver.Chrome(service=servico)

site = "https://queimadas.dgi.inpe.br/queimadas/sisam/v2/dados/download/"
navegador.get(site)

data_inicio = navegador.find_element(By.ID, "inicio")
data_final = navegador.find_element(By.ID, "final")
data_inicio.clear()

uf = navegador.find_element(By.ID, "uf")
select_object = Select(uf)

ano_inicial = 2000

#até 2019
#20
for i in range(20):

    data_inicio.clear()
    data_final.clear()

    data_inicio.send_keys("01/01/{}".format(ano_inicial + i))

    data_final.send_keys("31/12/{}".format(ano_inicial + i))
    #27
    for i in range(27):
        select_object = Select(uf)
        select_object.select_by_index(i)
        press_download = navegador.find_element(By.ID, "formsubmit").click()
