import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as Ec
import random

from utilities.Baseclass import BaseClass


class Country(BaseClass):
    #  Select Country page locators
    page_title = (By.XPATH, '//label[text()="Choose Country"]')
    checkbox = (By.CSS_SELECTOR, '.chkAgree')
    term_and_condition = (By.XPATH, '//a[text()="Terms & Conditions"]')
    proceed = (By.XPATH, '//button[text()="Proceed"]')
    select = '//select'
    Greenkart = '.greenLogo'

    def __init__(self, driver):
        self.driver = driver

    def Country_page_loading(self):
        # wait = WebDriverWait(self.driver, 10)
        # wait.until(Ec.presence_of_element_located((By.XPATH, '//label[text()="Choose Country"]')))
        self.wait_for_element_By_Xpath('//label[text()="Choose Country"]')
        print('Country choose page loaded successfully')

    def select_country_and_proceed(self):
        self.Select_value_from_dropdown(locator=Country.select, value='India')
        self.driver.find_element(*Country.checkbox).click()
        assert self.driver.find_element(*Country.term_and_condition).text == 'Terms & Conditions'
        self.driver.find_element(*Country.proceed).click()
        print('Test completed successfully')

    def return_to_homepage(self):
        self.wait_for_element_By_Css_selector('.greenLogo')
        page_title = self.driver.find_element(By.CSS_SELECTOR, Country.Greenkart).text
        assert page_title == 'GREENKART'
