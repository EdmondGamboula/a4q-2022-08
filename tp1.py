import time

from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By


def test_open_chrome():
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get("https://www.amazon.fr")
    barre_recherche = driver.find_element(By.XPATH, "//input[@id='twotabsearchtextbox']")
    barre_recherche.send_keys("Playstation 5" + Keys.ENTER)
    driver.quit()

def test_open_chrome2():
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get("https://www.amazon.fr")
    barre_recherche = driver.find_element(By.XPATH, "//input[@id='twotabsearchtextbox']")
    barre_recherche.send_keys("Playstation 5" + Keys.ENTER)
    selectionne = ouvrirnav.find_element(By.CSS_SELECTOR, "span.a-size-base-plus.a-color-base.a-text-normal")
    selectionne.Click()
    driver.quit()

def test_achat_playstation():
    ouvrirnav = webdriver.Chrome()
    ouvrirnav.maximize_window()
    ouvrirnav.get("https://www.amazon.fr")
    barre_recherche = driver.find_element(By.CSS_SELECTOR, "input.nav-input.nav-progressive-attribute[type=text]")
    barre_recherche.send_keys("Playstation 5")
    barre_recherche.Click()
    selectionne = ouvrirnav.find_element(By.CSS_SELECTOR, "span.a-size-base-plus.a-color-base.a-text-normal")
    selectionne.Click()
    panier = ouvrirnav.find_element(By.CSS_SELECTOR, "span.a-button-inner")
    panier.Click()

def test_carrefour():
    ouvrirnav = webdriver.Chrome()
    ouvrirnav.maximize_window()
    ouvrirnav.get("https://www.carrefour.fr/")
    cookies = ouvrirnav.find_element(By.CSS_SELECTOR, "div.banner-actions-container > button")
    cookies.click()
    barre_recherche = ouvrirnav.find_element(By.CSS_SELECTOR, "input.pl-input-text__input--text.pl-input-text__input--no-auto-zoom")
    barre_recherche.send_keys("biere 1664")
    barre_recherche.click()
    bierre = ouvrirnav.find_element(By.LINK_TEXT, "/p/biere-lager-blonde-sans-alcool-1664-3080216055442")
    bierre.click()
    acheter = ouvrirnav.find_element(By.CSS_SELECTOR, "span.pl-button__label > span")
    acheter.click()


def test_carrefour2():
    ouvrirnav = webdriver.Chrome()
    ouvrirnav.maximize_window()
    ouvrirnav.get("https://www.carrefour.fr/")
    cookies = ouvrirnav.find_element(By.XPATH, "//button[@id='onetrust-accept-btn-handler']")
    cookies.click()
    barre_recherche = ouvrirnav.find_element(By.XPATH, "//div[@class='pl-input-text-group pl-input-text-group--append-component header-search__bar']")
    barre_recherche.send_keys("biere 1664")
    barre_recherche.click()
    bierre = driver.find_element(By.LINK_TEXT, "/p/biere-lager-blonde-sans-alcool-1664-3080216055442")
    bierre.click()
    acheter = ouvrirnav.find_element(By.CSS_SELECTOR, "span.pl-button__label > span")
    retrait_magasin = driver.find_element
    livraison
    livraison_1h
    acheter.click()






