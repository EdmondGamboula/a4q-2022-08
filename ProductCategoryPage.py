from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait


class productCategoryPage():

    prod_selector = ".product-grid-item:not(.storetail) h2"

    def __init__(self, driver: webdriver.chrome):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)
        self.action = ActionChains(driver)

    def openProducts(self, index):
        # Function to open product by element
            liste_produits = self.driver.find_elements(By.CSS_SELECTOR, self.prod_selector)
            liste_produits[index].click()