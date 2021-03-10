from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from creds_n_info import *
import time
from selenium.webdriver.common.action_chains import ActionChains
import xlwt
Wbook = xlwt.Workbook()
Wsheet = Wbook.add_sheet('sheet1')
Wsheet.write(0,0,'No - ')
Wsheet.write(0,1,'Name')
Wsheet.write(0,2,'Main category')
# Wsheet.write(0,3,'Category Name')
Wsheet.write(0,3,'URL')
ch_path = 'chromedriver.exe'
driver = webdriver.Chrome(executable_path=ch_path)

driver.get('https://www.aosom.ca/item/soozier-upright-stationary-exercise-bike-indoor-cycling-bicycle~A90-144.html')
categories_1 = driver.find_elements(By.XPATH,'//li[@class="top-li"]')
count = 1
for cat1 in categories_1:
    name = ''
    url = ''
    head = ''
    hover = ActionChains(driver).move_to_element(cat1).perform()
    time.sleep(1)
    cat2 = cat1.find_element(By.CLASS_NAME,'belong-categories')
    cat_cols = cat2.find_elements(By.TAG_NAME,'dl')

    for cat_col in cat_cols:

        infos = cat_col.find_elements(By.TAG_NAME,'dd')
        for inf in infos:
            name = inf.find_element(By.TAG_NAME,'a').text
            url = inf.find_element(By.TAG_NAME,'a').get_attribute('href')
            print(name)
            print(url)

        Wsheet.write(count, 0, count)
        Wsheet.write(count, 1, name)
        Wsheet.write(count, 2, head)
        # Wsheet.write(count, 3, 'Category Name')
        Wsheet.write(count, 3, url)
        count = count + 1
    print('________________')
driver.quit()
Wbook.save('category.xlsx')