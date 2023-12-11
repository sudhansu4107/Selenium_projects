import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as Ec
import random

from utilities.Baseclass import BaseClass


class Trial(BaseClass):
    page_title = '//label[text()="Choose Country"]'
    checkbox = (By.CSS_SELECTOR, '.chkAgree')
    term_and_condition = (By.XPATH, '//a[text()="Terms & Conditions"]')
    proceed = (By.XPATH, '//button[text()="Proceed"]')

    def __init__(self, driver):
        self.driver = driver

    def Country_page_loading(self):
        self.wait_for_element_By_Xpath(Trial.page_title)
        print('Country choose page loaded successfully')