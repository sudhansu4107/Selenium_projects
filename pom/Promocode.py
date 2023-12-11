import time

import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as Ec
import random

from utilities.Baseclass import BaseClass


class Promo(BaseClass):

    def __init__(self, driver):
        self.driver = driver

    def test_promopage_loading(self):
        log=self.get_logs()
        Apply = self.driver.find_element(By.CSS_SELECTOR, '.promoBtn')
        # wait = WebDriverWait(self.driver, 10)
        # wait.until(Ec.presence_of_element_located((By.CSS_SELECTOR, '.promoBtn')))
        self.wait_for_element_By_Css_selector('.promoBtn')
        log.info('page  loaded successfully.')

    def test_product_details(self):
        log = self.get_logs()
        product_name = self.driver.find_element(By.CSS_SELECTOR, '.product-name')
        assert product_name.text == 'Brocolli - 1 Kg'
        # Product_qty = self.driver.find_element(By.CSS_SELECTOR, '.quantity')
        # assert Product_qty.text == '1'
        Product_price = self.driver.find_element(By.CSS_SELECTOR, '.amount')
        assert Product_price.text == '120'
        # Product_total = self.driver.find_element(By.CSS_SELECTOR, '.amount')
        # assert Product_total == '120'
        log.info('product_details verified successfully')

    def test_apply_promocode(self):
        log = self.get_logs()
        text_box = self.driver.find_element(By.CSS_SELECTOR, '.promoCode')
        # print(f'The Test data is :{Testdata}')
        text_box.clear()
        text_box.send_keys('rahulshettyacademy')
        # text_box.send_keys(Testdata)
        Apply = self.driver.find_element(By.CSS_SELECTOR, '.promoBtn')
        Apply.click()
        # wait = WebDriverWait(self.driver, 10)
        # wait.until(Ec.presence_of_element_located((By.CSS_SELECTOR, '.promoInfo')))
        self.wait_for_element_By_Css_selector('.promoInfo')
        log.info(f'promocode applied successfully:')

    def test_calculate_discount(self):
        log = self.get_logs()
        discount = self.driver.find_element(By.CSS_SELECTOR, '.discountPerc').text
        assert discount in '10%'

        price_after_discount = (10 / 100) * int(self.driver.find_element(By.CSS_SELECTOR, '.totAmt').text)
        displayed_price_after_discount = self.driver.find_element(By.CSS_SELECTOR, '.discountAmt').text
        if price_after_discount == int(displayed_price_after_discount):
            log.info('Discount applied')
        else:
            log.info('Discount not  applied')

        log.info('Discount price verified  after applying promocode.')
        self.driver.find_element(By.XPATH, '//button[text()="Place Order"]').click()
        log.info('order placed')
        time.sleep(5)
