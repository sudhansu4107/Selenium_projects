import inspect
import logging

import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as Ec


@pytest.mark.usefixtures('Browser')
class BaseClass:
    def get_logs(self):
        logname = inspect.stack()[1][3]
        logger = logging.getLogger(logname)
        filehandler = logging.FileHandler('G:\\Selenium\\Reports\\Logs\\pytest.log')
        formatter = logging.Formatter("%(asctime)s:%(levelname)s:%(name)s:%(message)s")
        filehandler.setFormatter(formatter)
        logger.addHandler(filehandler)
        logger.setLevel(logging.INFO)
        return logger

    def wait_for_element_By_Xpath(self, locator):
        wait = WebDriverWait(self.driver, 10)
        wait.until(Ec.presence_of_element_located((By.XPATH, locator)))

    def wait_for_element_By_Css_selector(self, locator):
        wait = WebDriverWait(self.driver, 10)
        wait.until(Ec.presence_of_element_located((By.CSS_SELECTOR, locator)))

    def wait_for_element_By_Xpath_Visible(self, locator):
        wait = WebDriverWait(self.driver, 10)
        wait.until(Ec.text_to_be_present_in_element((By.XPATH, locator),'ADD TO CART'))

    def wait_for_element_By_Css_Visible(self, locator):
        wait = WebDriverWait(self.driver, 10)
        wait.until(Ec.presence_of_element_located((By.CSS_SELECTOR, locator)))

    def Select_value_from_dropdown(self, locator, value):
        drp = Select(self.driver.find_element(By.XPATH, locator))
        drp.select_by_value(value)
