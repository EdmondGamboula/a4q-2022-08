import time

from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By


def test_open_chrome():
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get("https://www.amazon.fr")
    time.sleep(2)
    barre_recherche = driver.find_element(By.XPATH, "//input[@id='twotabsearchtextbox']")
    barre_recherche.send_keys("Playstation 5" + Keys.ENTER)
    time.sleep(2)
    driver.quit()