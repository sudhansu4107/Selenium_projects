import time
import sys
sys.path.append('G:\Selenium')
import pytest
from selenium.webdriver.common.by import By
from pom.Home import Kart
from pom.Promocode import Promo
from pom.choose_country import Country
from pom.trial import Trial
from testdata.promocode import Promo_coupons
from utilities.Baseclass import BaseClass


class Test_home(BaseClass):

    def test_Page_load(self):
        print('page loaded successfully.')
        obj = Kart(self.driver)
        obj.test_check_the_title_of_the_webpage()
        obj.test_Search_product()
        obj.test_Add_product_to_Cart()
        obj.test_Go_to_Cart()
        prm = Promo(self.driver)
        prm.test_promopage_loading()
        prm.test_product_details()
        prm.test_apply_promocode()
        prm.test_calculate_discount()
        country = Country(self.driver)
        country.Country_page_loading()
        country.select_country_and_proceed()
        country.return_to_homepage()
        print('Test passed successfully')

    @pytest.fixture(params=Promo_coupons.promo_codes)
    def Testdata(self, request):
        return request.param
