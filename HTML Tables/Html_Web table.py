import time

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


# Invoke the browser and navigate to the url
option=Options()
option.add_argument('--headless')
option.add_argument('--disable-gpu')
option.add_experimental_option("excludeSwitches",["ignore-certificate-errors"])
service_obj = Service(
    'C:\\Users\\9337098512\\OneDrive\\Desktop\SudhansuAutomation\\Automation Project\\Webdrivers\\chromedriver.exe')
driver = webdriver.Chrome(service=service_obj,options=option)
driver.get('https://rahulshettyacademy.com/AutomationPractice/')
print(f'The title of the Webpage is {driver.title}')
driver.maximize_window()

# Print the table content
flag = driver.find_element(By.XPATH, "//fieldset/legend [text()='Web Table Example']")
driver.execute_script("arguments[0].scrollIntoView();", flag)

# print all the tile of the webpage

total_rows=driver.find_elements(By.XPATH,'//table[1]/tbody[1]/tr/td[text()="Rahul Shetty"]')
print(f'The total number of rows found = {len(total_rows)}')

total_cols=driver.find_elements(By.XPATH,'//table[1]/tbody[1]/tr[2]/td')
print(f'The total number of columns found = {len(total_cols)}')

#print the title of the table
title=driver.find_elements(By.XPATH,'//tbody/tr/th')
for title_text in title:
    print(title_text.text, end="    ")
print()

# Print Each row of the table
for r in range(1,len(total_rows)+1):
    for c in range(1,4):
        # print(r,c)
        print(driver.find_element(By.XPATH,'//table[1]/tbody[1]/tr['+str(r)+']/td['+str(c)+']').text,end=" ")
    print()


print("programme execution completed.")

# Programme output
# The title of the Webpage is Practice Page
# The total number of rows found = 10
# The total number of columns found = 7
# Instructor    Course    Price
# Rahul Shetty Selenium Webdriver with Java Basics + Advanced + Interview Guide 30
# Rahul Shetty Learn SQL in Practical + Database Testing from Scratch 25
# Rahul Shetty Appium (Selenium) - Mobile Automation Testing from Scratch 30
# Rahul Shetty WebSecurity Testing for Beginners-QA knowledge to next level 20
# Rahul Shetty Learn JMETER from Scratch - (Performance + Load) Testing Tool 25
# Rahul Shetty WebServices / REST API Testing with SoapUI 35
# Rahul Shetty QA Expert Course :Software Testing + Bugzilla + SQL + Agile 25
# Rahul Shetty Master Selenium Automation in simple Python Language 25
# Rahul Shetty Advanced Selenium Framework Pageobject, TestNG, Maven, Jenkins,C 20
# programme execution completed.
