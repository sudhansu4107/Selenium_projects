import sys

sys.path.append("G:\\Selenium")

from testdata.Excel_Data_extraction import Excel_data
from pom.Calculate_items_price import Test_Excel_record

from utilities.Baseclass import BaseClass

obj = Excel_data()
product_list = obj.Fetch_Productname()
Qty_list = obj.Fetch_Qty()


# print(f'The product_list={product_list},The Qty is ;{Qty_list}')


class Test_Datadriven_Add_product(BaseClass):
    Total_amt = []

    def test_Datadriven_Add_to_cart(self):
        Datadriven = Test_Excel_record(self.driver)
        print(f'The product_list={len(product_list)},The Qty is ;{len(Qty_list)}')
        Datadriven.search_and_add_to_cart(product_list, Qty_list)
        print(f'Price_List is {Test_Excel_record.Price_List}')
        obj.Update_Item_price(Item_price=Test_Excel_record.price_Quotes)
        for i in range(len(Qty_list)):
            Test_Datadriven_Add_product.Total_amt.append(int(Test_Excel_record.price_Quotes[i])*int(Qty_list[i]))
        print(Test_Datadriven_Add_product.Total_amt)
        obj.Update_Total_amt(Total_amt=Test_Datadriven_Add_product.Total_amt)
        Datadriven.go_to_cart()
