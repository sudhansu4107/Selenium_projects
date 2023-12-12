from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

from utilities.Baseclass import BaseClass


class Item_validation(BaseClass):
    def __init__(self, driver):
        self.driver = driver

    def search_and_validate_items(self, load_date):
        print(f'Loop started ,  Test Data={load_date}')
        search_box = self.driver.find_element(By.CSS_SELECTOR, '.search-keyword')
        search_box.clear()
        search_box.send_keys(load_date)
        self.driver.find_element(By.CLASS_NAME, 'search-button').click()
        self.wait_for_element_By_Css_selector('.product-name')
        print('Product is  successfully searched')
        Result = self.driver.find_element(By.XPATH, '//button[text()="ADD TO CART"]')
        if Result.text == load_date:
            print('Condition satisfied')
        else:
            print('condition false')
