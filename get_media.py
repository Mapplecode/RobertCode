import xlwt
import xlrd
import urllib
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
Wbook = xlwt.Workbook()
Wsheet = Wbook.add_sheet('sheet1')
options = webdriver.ChromeOptions()
options.headless = True
Rbook = xlrd.open_workbook('product_list.xlsx')
Rsheet = Rbook.sheet_by_index(0)
ch_path = '/home/oem/PycharmProjects/robert(beaustore)/chromedriver'
driver = webdriver.Chrome(executable_path=ch_path,chrome_options=options)
data_list = list()
count = 0
price = ''
SKU = ''
# Wsheet.write(count, 1, str('NAME'))
# Wsheet.write(count, 2, str('Available'))
Wsheet.write(count, 1, str('SKU'))
Wsheet.write(count, 2, str('images'))
# Wsheet.write(count, 5, str('Categories'))
# for i in range(1,Rsheet.nrows):
#     print(Rsheet.cell_value(i,2))
#     url = (Rsheet.cell_value(i,2))
url = 'https://www.aosom.ca/item/homcom-coat-rack-wooden-hall-tree-cabinet-shoe-bench-with-rack-3-hooks~837-100.html'
driver.get(str(url))
count = count+1
try:
    time.sleep(1)
    driver.find_element(By.TAG_NAME, 'body').send_keys(Keys.ESCAPE)
except:
    pass
list_cat = list()
b= True
while(b):
    img_clicks = driver.find_element(By.CLASS_NAME,'swiper-zoomer-button-next')
    if 'disabled' in img_clicks.get_attribute('class'):
        b=False
    else:
        img_clicks.click()
        time.sleep(.5)
        print(driver.find_element(By.CLASS_NAME,'square-box').find_element(By.TAG_NAME,'img').get_attribute('src'))
        time.sleep(.5)

# h1 = driver.find_element(By.TAG_NAME,'h1')
# spans = driver.find_element(By.CLASS_NAME,'right-product').find_elements(By.TAG_NAME,'span')
# for i in spans:
#     if 'secondary--text' in i.get_attribute('class'):
#         print(i.text)
#         price = i.text
#     elif 'ml-2 font-weight-medium f14' in i.get_attribute('class'):
#         print(i.text)
#         SKU = i.text
# try:
#     stock = driver.find_element(By.ID,'add-btn').text
#     print(stock)
#     stock = 'In Stock'
# except:
#     out = driver.find_elements(By.CLASS_NAME,'v-btn__content')
#     OUT_OF_STOCK = False
#     stock = 'Out of Stock'
#     for st in out:
#         if 'Notify Me When Available' in st.text:
#             OUT_OF_STOCK=True
#     if OUT_OF_STOCK == True:
#         print('OUT OF STOCK')
# uls = driver.find_elements(By.TAG_NAME,'ul')
# for ul in uls:
#     if 'v-breadcrumbs' in ul.get_attribute('class'):
#         list_cat.append(ul.text)
# print(list_cat)
# print(h1.text)
    # Wsheet.write(count, 1, str(h1.text))
    # Wsheet.write(count, 2, str(stock))
    # Wsheet.write(count, 3, str(SKU))
    # Wsheet.write(count, 4, str(price))
    # Wsheet.write(count, 5, str(list_cat))
    # Wbook.save('all_products.xlsx')

