import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as Ec
import random

from utilities.Baseclass import BaseClass


class Kart(BaseClass):
    # Home  page locators
    Title = (By.CSS_SELECTOR, '.brand')
    Search_box = (By.CSS_SELECTOR, '.search-keyword')
    Search_icon = (By.CSS_SELECTOR, '.search-button')
    Total_items = (By.XPATH, '//button[text()="ADD TO CART"]')
    Product_names = (By.CSS_SELECTOR, '.product-name')
    item_price = (By.CSS_SELECTOR, '.product-price')
    Product_prices = ''
    Number_of_Items_added_to_cart = (By.XPATH, '//table/tbody/tr[1]/td[3]')
    Price_of_the_Cart_Items = (By.XPATH, '//table/tbody/tr[2]/td[3]')
    Cart_icon = (By.CSS_SELECTOR, '.cart-icon')
    Proceed_to_checkout = (By.XPATH, '//button[text()="PROCEED TO CHECKOUT"]')
    empty_cart = (By.XPATH, '(//h2[text()="You cart is empty!"])[1]')

    def __init__(self, driver):
        self.driver = driver

    def test_check_the_title_of_the_webpage(self):
        Title_text = self.driver.find_element(*Kart.Title)
        print(Title_text.text)
        assert Title_text.text == 'GREENKART'

    def test_Search_product(self):
        self.driver.find_element(*Kart.Search_box).send_keys('Bro')
        self.driver.find_element(*Kart.Search_icon).click()
        self.wait_for_element_By_Xpath('//button[text()="ADD TO CART"]')
        self.Product_prices = self.driver.find_element(*Kart.item_price)
        print(f'Price of  the product is {self.Product_prices.text}')

    # select  the Quantity  randomly and Add to the cart
    def test_Add_product_to_Cart(self):
        Quantity_Selected = random.randint(1, 10)
        print(f'The random Qty selected is  :{Quantity_Selected}')
        for i in range(Quantity_Selected):
            self.driver.find_element(*Kart.Total_items).click()
            self.wait_for_element_By_Css_selector('.added')
        print('Required Quantity is selected.')

        # Check the added  products price and Quantity displaying on the top right
        Cart_added_item_Qty = self.driver.find_element(*Kart.Number_of_Items_added_to_cart)
        print(f'Cart_added_item_Qty:{int(Cart_added_item_Qty.text)}')
        Cart_added_item_price = self.driver.find_element(*Kart.Price_of_the_Cart_Items)
        print(f'Cart_added_item_price:{int(Cart_added_item_price.text)}')
        price = int(self.Product_prices.text) * Quantity_Selected
        print(f'The calculated price is :{price}')
        if int(Cart_added_item_Qty.text) == 1 and int(Cart_added_item_price.text) == price:
            print('condition satisfied')
        else:
            print('Condition is false')

    def test_Go_to_Cart(self):
        self.driver.find_element(*Kart.Cart_icon).click()
        self.wait_for_element_By_Xpath('//button[text()="PROCEED TO CHECKOUT"]')
        self.driver.find_element(*Kart.Proceed_to_checkout).click()

    def test_empty_cart(self):
        self.driver.find_element(*Kart.Cart_icon).click()
        self.wait_for_element_By_Css_selector('.empty-cart')
        cart_text = self.driver.find_element(*Kart.empty_cart).text
        assert cart_text=='You cart is empty!'
        self.driver.find_element(*Kart.Cart_icon).click()


    print('Test passed successfully')
