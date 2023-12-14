import time

from selenium.webdriver.common.by import By

from testdata.Excel_Data_extraction import Excel_data
from utilities.Baseclass import BaseClass


class Test_Excel_record(BaseClass):
    Item_Dict = {}
    Price_List = {}
    price_Quotes = []
    # Home  page locators
    Title = (By.CSS_SELECTOR, '.brand')
    Search_box = (By.CSS_SELECTOR, '.search-keyword')
    Search_icon = (By.CSS_SELECTOR, '.search-button')
    Total_items = (By.XPATH, '//button[text()="ADD TO CART"]')
    Product_names = (By.CSS_SELECTOR, '.product-name')
    item_price = (By.XPATH, '//div[@class="product"]')
    Product_prices = ''
    Number_of_Items_added_to_cart = (By.XPATH, '//table/tbody/tr[1]/td[3]')
    Price_of_the_Cart_Items = (By.XPATH, '//table/tbody/tr[2]/td[3]')
    Cart_icon = (By.CSS_SELECTOR, '.cart-icon')
    Proceed_to_checkout = (By.XPATH, '//button[text()="PROCEED TO CHECKOUT"]')
    empty_cart = (By.XPATH, '(//h2[text()="You cart is empty!"])[1]')
    Qty_locator = (By.XPATH, '//input[@class="quantity"]')
    Cart_rows = '(//ul[@class="cart-items"])[1]/li'
    cart_product_name = '(//ul[@class="cart-items"])[1]/li[1]/div[1]/p[@class="product-name"]'
    cart_product_price = '(//ul[@class="cart-items"])[1]/li[1]/div[1]/p[@class="product-price"]'

    def __init__(self, driver):
        self.driver = driver

    def search_and_add_to_cart(self, product_list, Qty_list):
        print('Search started')
        for i in range(len(product_list)):
            Enter = self.driver.find_element(*Test_Excel_record.Search_box)
            Enter.clear()
            time.sleep(5)
            Enter.send_keys(product_list[i])
            self.driver.find_element(*Test_Excel_record.Search_icon).click()
            self.wait_for_element_By_Xpath('//button[text()="ADD TO CART"]')
            self.driver.find_element(*Test_Excel_record.Qty_locator).clear()
            self.driver.find_element(*Test_Excel_record.Qty_locator).send_keys(Qty_list[i])
            get_price = self.driver.find_element(*Test_Excel_record.item_price).text
            get_price = int(get_price.split('\n')[1])
            # Excel_data.Update_Item_price(get_price)
            product_name = product_list[i]
            Test_Excel_record.Price_List[product_name] = get_price
            Test_Excel_record.price_Quotes.append(get_price)
            print(f'Following items added to tuple :{Test_Excel_record.Price_List}')
            self.driver.find_element(*Test_Excel_record.Total_items).click()
            self.wait_for_element_By_Xpath('//button[text()="ADD TO CART"]')
            print(f'The {product_list[i]} added successfully.')

    def go_to_cart(self):
        self.driver.find_element(*Test_Excel_record.Cart_icon).click()
        self.wait_for_element_By_Xpath('//button[text()="PROCEED TO CHECKOUT"]')
        rows = self.driver.find_elements(By.XPATH, Test_Excel_record.Cart_rows)
        print(1, len(rows) + 1)
        for i in range(1, len(rows) + 1):
            items_name = self.driver.find_element(By.XPATH, '(//ul[@class="cart-items"])[1]/li[' + str(
                i) + "]/div[1]/p[@class=" + "'product-name'" + ']')
            item_price = self.driver.find_element(By.XPATH, '(//ul[@class="cart-items"])[1]/li[' + str(
                i) + "]/div[1]/p[@class=" + "'product-price'" + ']')
            print(items_name, item_price)
            Test_Excel_record.Item_Dict[items_name.text] = item_price.text
        time.sleep(20)
        print(Test_Excel_record.Item_Dict)
        keys = (Test_Excel_record.Item_Dict.keys())

        for key in keys:
            if Test_Excel_record.Price_List.get(key) == Test_Excel_record.Item_Dict.get(key):
                print('Condition satisfied')
            else:
                print('All the item are not added to the cart.')