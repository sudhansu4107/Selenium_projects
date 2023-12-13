import pytest
from selenium.webdriver.common.by import By

from utilities.Baseclass import BaseClass


class Search_product(BaseClass):
    product_list = []
    product_name_locator=(By.XPATH, '//div//h4[@class="product-name"]')

    def __init__(self, driver):
        self.driver = driver

    def Fetchall_products_name(self):
        product_obj = self.driver.find_elements(*Search_product.product_name_locator)
        for i in product_obj:
            Search_product.product_list.append(i.text)
        print(f'The final product list  is :{Search_product.product_list}')
        return Search_product.product_list


