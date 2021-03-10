from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from creds_n_info import *
import time


USERNAME_ = 'Administator'
PASSWORD_ = 'Africa12~'
ch_path = 'chromedriver.exe'

login_page = 'https://beaustore.store/wp-admin/'
database_url = 'https://beaustore.store/wp-admin/edit.php?post_status=publish&post_type=product'


driver = webdriver.Chrome(executable_path=ch_path)
driver.get(login_page)
driver.find_element(By.ID,'user_login').send_keys(USERNAME_)
password =  driver.find_element(By.ID,'user_pass')
password.send_keys(PASSWORD_)
password.send_keys(Keys.ENTER)
time.sleep(2)
driver.get(database_url)
time.sleep(1)

LIST_OF_PRODUCTS_TODAY = []
product_list = driver.find_elements(By.CLASS_NAME,'status-publish')
for prd in product_list:
    product_dict = {}
    tds = prd.find_elements(By.TAG_NAME,'td')
    for td in tds:
        if td.get_attribute('data-colname') == 'Date':
            product_dict['Date'] = str(td.text)
        if td.get_attribute('data-colname') == 'Name':
            product_dict['Name'] = str(td.text)
        if td.get_attribute('data-colname') == 'SKU':
            product_dict['SKU'] = str(td.text)
        if td.get_attribute('data-colname') == 'Stock':
            product_dict['Stock'] = str(td.text)
        if td.get_attribute('data-colname') == 'Price':
            product_dict['Price'] = str(td.text)
    LIST_OF_PRODUCTS_TODAY.append(product_dict)

for i in LIST_OF_PRODUCTS_TODAY:
    print(i)