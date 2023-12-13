import time

from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

from utilities.Baseclass import BaseClass


class Item_validation(BaseClass):
    Search_keyword = By.CSS_SELECTOR, '.search-keyword'
    Search_btn = (By.CLASS_NAME, 'search-button')
    product_name = (By.XPATH, '//div/h4[@class="product-name"]')

    def __init__(self, driver):
        self.driver = driver

    def search_and_validate_items(self, load_date):
        print(f'Loop started ,  Test Data={load_date}')
        search_box = self.driver.find_element(*Item_validation.Search_keyword)
        search_box.clear()
        search_box.send_keys(load_date)
        self.driver.find_element(*Item_validation.Search_btn).click()
        self.wait_for_element_By_Css_selector('.product-name')
        print('Product is  successfully searched')
        time.sleep(3)
        Result = self.driver.find_element(*Item_validation.product_name).text
        if Result == load_date:
            print('Condition satisfied')
        else:
            print(f'condition false:{Result}')
