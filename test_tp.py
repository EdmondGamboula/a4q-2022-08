import time
from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By

def test_panier():
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get("https://www.carrefour.fr/")
    time.sleep(2)
    cookies = driver.find_element(By.XPATH, "//button[@id='onetrust-accept-btn-handler']")
    cookies.click()
    barre_recherche = driver.find_element(By.XPATH, "//input[@data-testid='input-control']")
    barre_recherche.send_keys("1664")
    bouton_recherche = driver.find_element(By.XPATH, "//button[@type='submit']")
    bouton_recherche.click()
    biere = driver.find_element(By.XPATH, "//li[@style='order: 1;']//a//img")
    biere.click()
    time.sleep(2)
    acheter = driver.find_element(By.XPATH, "//span[@class='pl-button__label']//span")
    acheter.click()
    time.sleep(2)
    retrait_en_magasin = driver.find_element(By.XPATH, "//section[@data-testid='pill-informations']//span[contains(text(),'Drive')]")
    livraison =driver.find_element(By.XPATH, "//section[@data-testid='pill-informations']//span[contains(text(),'Livraison')]")
    livraison_1h = driver.find_element(By.XPATH, "//section[@data-testid='pill-informations']//span[contains(text(),'Livraison 1h')]")
    # (peut être fait de cette maniere aussi , la variable retourne le text de l'autre cote des egales et onverifie si il so identique )
    # assert retrait_en_magasin.text == 'Drive\nRetrait gratuit en magasin'
    # (peut être fait de cette maniere aussi ) assert delivery24.text == 'Livraison\nVotre plein de course en 24h'
    # (peut être fait de cette maniere aussi ) assert delivery1.text == 'Livraison 1h\nVos courses d’appoint en 1h'
    assert "Drive" in retrait_en_magasin.text
    assert "Livraison" in livraison.text
    assert "Livraison 1h" in livraison_1h.text
    time.sleep(2)
    driver.quit()