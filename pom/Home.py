import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as Ec
import random

from utilities.Baseclass import BaseClass


class Kart(BaseClass):
    def __init__(self, driver):
        self.driver = driver
        self.Search_box = self.driver.find_element(By.CSS_SELECTOR, '.search-keyword')
        self.Search_icon = self.driver.find_element(By.CSS_SELECTOR, '.search-button')
        self.Total_items = self.driver.find_element(By.XPATH, '//button[text()="ADD TO CART"]')
        self.Product_names = self.driver.find_elements(By.CSS_SELECTOR, '.product-name')
        self.Product_prices = ''
        self.Number_of_Items_added_to_cart = self.driver.find_element(By.XPATH, '//table/tbody/tr[1]/td[3]')
        self.Price_of_the_Cart_Items = self.driver.find_element(By.XPATH, '//table/tbody/tr[2]/td[3]')
        self.Cart_icon = self.driver.find_element(By.CSS_SELECTOR, '.cart-icon')

    def test_check_the_title_of_the_webpage(self):
        Title_text = self.driver.find_element(By.CSS_SELECTOR, '.brand')
        print(Title_text.text)
        assert Title_text.text == 'GREENKART'

    def test_Search_product(self):
        self.Search_box.send_keys('Bro')
        self.Search_icon.click()
        # wait = WebDriverWait(self.driver, 10)
        # wait.until(Ec.element_to_be_clickable((By.XPATH, '//button[text()="ADD TO CART"]')))
        self.wait_for_element_By_Xpath('//button[text()="ADD TO CART"]')
        self.Product_prices = self.driver.find_element(By.CSS_SELECTOR, '.product-price')
        print(f'Price of  the product is {self.Product_prices.text}')

    # select  the Quantity  randomly and Add to the cart
    def test_Add_product_to_Cart(self):
        Quantity_Selected = random.randint(1, 10)
        print(f'The random Qty selected is  :{Quantity_Selected}')
        for i in range(Quantity_Selected):
            self.Total_items.click()
            # wait = WebDriverWait(self.driver, 10)
            # wait.until(Ec.presence_of_element_located((By.CLASS_NAME, 'added')))
            self.wait_for_element_By_Css_selector('.added')
        print('Required Quantity is selected.')

        # Check the added  products price and Quantity displaying on the top right
        Cart_added_item_Qty = self.driver.find_element(By.XPATH, '//table/tbody/tr[1]/td[3]')
        print(f'Cart_added_item_Qty:{int(Cart_added_item_Qty.text)}')
        Cart_added_item_price = self.driver.find_element(By.XPATH, '//table/tbody/tr[2]/td[3]')
        print(f'Cart_added_item_price:{int(Cart_added_item_price.text)}')
        price = int(self.Product_prices.text) * Quantity_Selected
        print(f'The calculated price is :{price}')
        if int(Cart_added_item_Qty.text) == 1 and int(Cart_added_item_price.text) == price:
            print('condition satisfied')
        else:
            print('Condition is false')

    def test_Go_to_Cart(self):
        self.Cart_icon.click()
        # wait = WebDriverWait(self.driver, 10)
        # wait.until(Ec.element_to_be_clickable((By.XPATH, '//button[text()="PROCEED TO CHECKOUT"]')))
        self.wait_for_element_By_Xpath('//button[text()="PROCEED TO CHECKOUT"]')
        self.driver.find_element(By.XPATH, '//button[text()="PROCEED TO CHECKOUT"]').click()

    print('Test passed successfully')
