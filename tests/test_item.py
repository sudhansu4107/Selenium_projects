import pytest
from selenium.webdriver.common.by import By
import sys

sys.path.append('G:\\Selenium')
from pom.Validate_items import Item_validation
from pom.collect_items import Search_product
from testdata.Items_names import item
from utilities.Baseclass import BaseClass

Veg_names = []


class Test_search(BaseClass):

    def test_search_product(self):
        Search = Search_product(self.driver)
        global Veg_names
        Veg_names = Search.Fetchall_products_name()
        print(f'The array contains following items ={Veg_names}')

    def test_Datadriven(self, load_date):
        Val = Item_validation(self.driver)
        Val.search_and_validate_items(load_date)

    @pytest.fixture(params=item.Veg_array)
    def load_date(self, request):
        return request.param

        # Search.Validate_product_name(self.TestData)
