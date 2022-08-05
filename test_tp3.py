import time
from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains


def openProduct(driver,index):
    liste_produits = driver.find_elements(By.CSS_SELECTOR, ".product-grid-item:not(.storetail) h2")
    liste_produits[index].click()


def test_carrefour():
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get("https://www.carrefour.fr/")
    wait = WebDriverWait(driver, 10)
    action = ActionChains(driver)
    cookies_button = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "#onetrust-accept-btn-handler")))
    cookies_button.click()
    hamb_button = driver.find_element(By.CSS_SELECTOR, ".mainbar__nav-toggle-icon")
    hamb_button.click()

    # pour faire bouger un element sur un menu
    #epice_sale = driver.find_element(By.CSS_SELECTOR, ".nav-item__icon img[alt='Epicerie salée']")
    epice_sale = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, ".nav-item__icon img[alt='Epicerie salée']")))
    action.move_to_element(epice_sale)
    action.perform()

    # pate_riz = driver.find_element(By.CSS_SELECTOR, ".nav-item a[href='/r/epicerie-salee/pates-riz-feculents']")
    pate_riz = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "li.nav-item #data-menu-level-2_R12F05]")))
    action.move_to_element(pate_riz)
    action.perform()


    #pate = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, ".nav-item a[href='/r/epicerie-salee/pates-riz-feculents/pates']")))
    pate = driver.find_element(By.CSS_SELECTOR, ".nav-item a[href='/r/epicerie-salee/pates-riz-feculents/pates']")
    pate.click()

    openProduct(driver,2)

    acheter = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "button.pl-button.pl-button--primary.add-to-cart__plus")))
    acheter.click()
    time.sleep(1)
    driv = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "input[name='PICKING_DRIVE-picker']")))
    driv.click()
    text_entrer = driver.find_element(By.CSS_SELECTOR, "input[aria-label='Saisir un code postal ou une ville']")
    text_entrer.send_keys("75001" + Keys.ENTER)
    choix = driver.find_element(By.CSS_SELECTOR, "h4.ds-title.ds-title--s")
    choix.click()







