import schedule
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options


def marcar_salida():
    print("Se inicio")
    options = Options()

    driver = webdriver.Chrome(options=options)
    driver.get("https://app.ctrlit.cl/ctrl/dial/web/KqpFkRElr7")

    btn_salida = driver.find_element(by=By.CLASS_NAME, value="btn-warning")


    btn_salida.click()
    # 74761212  dni de prueba

    btn_dni = driver.find_elements(by=By.CLASS_NAME, value="digits")

    btn_dni[6].click()
    btn_dni[3].click()
    btn_dni[6].click()
    btn_dni[5].click()
    btn_dni[0].click()
    btn_dni[1].click()
    btn_dni[0].click()
    btn_dni[1].click()

    btn_submit = driver.find_element(by=By.CLASS_NAME,value="pad-action")


    btn_submit.click()
    time.sleep(5)

def marcar_entrada():
    print("Se inicio")
    options = Options()

    driver = webdriver.Chrome(options=options)
    driver.get("https://app.ctrlit.cl/ctrl/dial/web/KqpFkRElr7")

    btn_entrada = driver.find_element(by=By.CLASS_NAME, value="btn-primary")


    btn_entrada.click()

    btn_dni = driver.find_elements(by=By.CLASS_NAME, value="digits")

    btn_dni[6].click()
    btn_dni[3].click()
    btn_dni[6].click()
    btn_dni[5].click()
    btn_dni[0].click()
    btn_dni[1].click()
    btn_dni[0].click()
    btn_dni[1].click()




hora_salida = "19:39"
hora_entrada = "19:41"

schedule.every().day.at(hora_salida).do(marcar_salida)
schedule.every().day.at(hora_entrada).do(marcar_entrada)

while True:
    print("escuchando")
    schedule.run_pending()
    time.sleep(1)


# btn_confirmacion = driver.find_element(by=By.CLASS_NAME,value="boton")
# btn_confirmacion.click()

# driver.quit()

