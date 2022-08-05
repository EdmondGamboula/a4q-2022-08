from lib2to3.pgen2 import driver

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class homePage():

    close_cookie_button_selector = (By.ID, "onetrust-accept-btn-handler")
    hamburger_selector = "#data-rayons"
    epicerie_salee_selector = ".nav-item__menu-link [alt='Epicerie salée']"
    feculent_selector = "#data-menu-level-1_R12 > li:nth-child(7)"
    pates_selector = "#data-menu-level-2_R12F05 > li:nth-child(3)"

    def __init__(self, driver: webdriver.chrome):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)
        self.action = ActionChains(driver)


    def closeCookies(self):

        closeCookieButton = self.wait.until(expected_conditions.element_to_be_clickable(self.close_cookie_button_selector))
        closeCookieButton.click()
        self.wait.until(expected_conditions.invisibility_of_element_located(self.close_cookie_button_selector))

    def open_menu(self):

        hamburger_button = self.driver.find_element(By.CSS_SELECTOR, self.hamburger_selector)
        hamburger_button.click()

    def open_epicerie_salee(self):

        epicerie_salee = self.wait.until(expected_conditions.element_to_be_clickable((By.CSS_SELECTOR, self.epicerie_salee_selector)))
        self.action.move_to_element(epicerie_salee)
        self.action.perform()

    def open_pates_riz(self):

        feculent = self.wait.until(expected_conditions.element_to_be_clickable((By.CSS_SELECTOR, self.feculent_selector)))
        self.action.move_to_element(feculent)
        self.action.perform()

    def open_pates(self):

        pates = self.driver.find_element(By.CSS_SELECTOR, self.pates_selector)
        pates.click()