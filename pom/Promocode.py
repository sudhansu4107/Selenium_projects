import time

import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as Ec
import random

from utilities.Baseclass import BaseClass


class Promo(BaseClass):
    Apply_btn = (By.CSS_SELECTOR, '.promoBtn')
    product_name_locator = (By.CSS_SELECTOR, '.product-name')
    Product_price_locator = (By.CSS_SELECTOR, '.amount')
    text_box_locator = (By.CSS_SELECTOR, '.promoCode')
    Discount_locator = (By.CSS_SELECTOR, '.discountPerc')
    total_amt = (By.CSS_SELECTOR, '.totAmt')
    Discount_amt = (By.CSS_SELECTOR, '.discountAmt')
    place_order = (By.XPATH, '//button[text()="Place Order"]')

    def __init__(self, driver):
        self.driver = driver

    def test_promopage_loading(self):
        log = self.get_logs()
        Apply = self.driver.find_element(*Promo.Apply_btn)
        self.wait_for_element_By_Css_selector('.promoBtn')
        log.info('page  loaded successfully.')

    def test_product_details(self):
        log = self.get_logs()
        product_name = self.driver.find_element(*Promo.product_name_locator)
        assert product_name.text == 'Brocolli - 1 Kg'
        # Product_qty = self.driver.find_element(By.CSS_SELECTOR, '.quantity')
        # assert Product_qty.text == '1'
        Product_price = self.driver.find_element(*Promo.Product_price_locator)
        assert Product_price.text == '120'
        # Product_total = self.driver.find_element(By.CSS_SELECTOR, '.amount')
        # assert Product_total == '120'
        log.info('product_details verified successfully')

    def test_apply_promocode(self):
        log = self.get_logs()
        text_box = self.driver.find_element(*Promo.text_box_locator)
        # print(f'The Test data is :{Testdata}')
        text_box.clear()
        text_box.send_keys('rahulshettyacademy')
        # text_box.send_keys(Testdata)
        Apply = self.driver.find_element(*Promo.Apply_btn)
        Apply.click()
        # wait = WebDriverWait(self.driver, 10)
        # wait.until(Ec.presence_of_element_located((By.CSS_SELECTOR, '.promoInfo')))
        self.wait_for_element_By_Css_selector('.promoInfo')
        log.info(f'promo-code applied successfully:')

    def test_calculate_discount(self):
        log = self.get_logs()
        discount = self.driver.find_element(*Promo.Discount_locator).text
        assert discount in '10%'

        price_after_discount = (10 / 100) * int(self.driver.find_element(*Promo.total_amt).text)
        displayed_price_after_discount = self.driver.find_element(*Promo.Discount_amt).text
        if price_after_discount == int(displayed_price_after_discount):
            log.info('Discount applied')
        else:
            log.info('Discount not  applied')

        log.info('Discount price verified  after applying promo-code.')
        self.driver.find_element(*Promo.place_order).click()
        log.info('order placed')
        time.sleep(5)
