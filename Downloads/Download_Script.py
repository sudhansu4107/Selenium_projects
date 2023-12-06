import time

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

URL = 'https://demoqa.com/upload-download'
prefs = {"download.default_directory": "C:\\Users\\9337098512\\OneDrive\\Desktop"
                                       "\\SudhansuAutomation\\Automation "
                                       "Project\\Downloads"}
# Invoke the browser and navigate to the url
option = Options()
option.add_argument('--headless')
option.add_argument('--disable-gpu')
option.add_experimental_option('prefs', prefs)
option.add_experimental_option("excludeSwitches", ["ignore-certificate-errors"])
service_obj = Service(
    'C:\\Users\\9337098512\\OneDrive\\Desktop\SudhansuAutomation\\Automation Project\\Webdrivers\\chromedriver.exe')
driver = webdriver.Chrome(service=service_obj, options=option)
driver.get(URL)
print(f'The title of the Webpage is {driver.title}')
driver.maximize_window()

# Upload the file
Choose_file = driver.find_element(By.ID, 'uploadFile')
Choose_file.send_keys(
    "C:\\Users\\9337098512\\OneDrive\\Desktop\\SudhansuAutomation\\Automation Project\\Files\\Test1_Excel.xlsx")

# Wait for the file to be uploaded
print('Enter into explicit wait ')
print(driver.find_element(By.ID, 'uploadedFilePath').text)
wait = WebDriverWait(driver, 10)
wait.until(EC.presence_of_element_located((By.ID, 'uploadedFilePath')))

# Download the File
Download = driver.find_element(By.ID, 'downloadButton')
Download.click()

print('Execution completed.')
