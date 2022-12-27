import time

from selenium import webdriver
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

def moverAbajoLista(driver):
    dropdown = driver.find_element(By.XPATH, '//*[@id="select2-boletinCalificacionesAlumno-container"]')
    ActionChains(driver).move_to_element(dropdown).click(dropdown).send_keys(Keys.ARROW_DOWN).send_keys(Keys.ENTER).click(dropdown).perform()

def generarTest(driver):
    paginaWeb = 'https://xhendra.ar/curso/details/35681'
    driver.get(paginaWeb)
    driver.maximize_window()

    time.sleep(4)
    usr = driver.find_element(By.NAME, 'username')
    usr.send_keys('Lramiro')
    password = driver.find_element(By.NAME, 'password')
    password.send_keys('Ramiro2003')
    ingreso = driver.find_element(By.XPATH, '//*[@id="kt_login_v2"]/div[1]/div/div[1]/div[2]/form/div[4]/button')
    ingreso.send_keys(Keys.ENTER)
    time.sleep(10) #para que cargue bien toda la pagina
    obsGlobales = driver.find_element(By.XPATH, '//*[@id="kt_page_portlet"]/div[1]/div[1]/div/ul/li[5]/a')
    obsGlobales.click()

    time.sleep(10)
    moverAbajoLista(driver)

    time.sleep(10)

def __main__():
    # dependiendo de la maquina quizas hay que cambiar el PATH al driver
    # o en algunos casos se puede omitir completamente
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    generarTest(driver)
    driver.close()

if __name__ == '__main__':
    __main__()