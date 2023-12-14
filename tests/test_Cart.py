import sys
sys.path.append('G:\\Selenium')
from pom.Home import Kart
from utilities.Baseclass import BaseClass


class Test_cart_items(BaseClass):
    def test_empty_cart(self):
        home=Kart(self.driver)
        home.test_check_the_title_of_the_webpage()
        home.test_empty_cart()
