import xlwt
import xlrd
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
Wbook = xlwt.Workbook()
Wsheet = Wbook.add_sheet('sheet1')

Rbook = xlrd.open_workbook('category.xlsx')
Rsheet = Rbook.sheet_by_index(0)
ch_path = 'chromedriver.exe'
driver = webdriver.Chrome(executable_path=ch_path)
data_list = list()
count = 1
for read in range(1,Rsheet.nrows):
    data_dict = {}
    url = Rsheet.cell_value(read,3)
    print(url)

    if '/brand/' not in Rsheet.cell_value(read,3):
        driver.get(Rsheet.cell_value(read, 3))
        print(Rsheet.cell_value(read,3))
        b = True
        while(b == True):
            try:
                time.sleep(1)
                driver.find_element(By.TAG_NAME, 'body').send_keys(Keys.ESCAPE)
            except:
                pass
            products = driver.find_elements(By.TAG_NAME,'a')
            for pt in products:
                try:
                    item_url = pt.get_attribute('href')
                    if item_url != None:
                        if 'item' in item_url:
                            print(item_url)
                            Wsheet.write(count, 0, Rsheet.cell_value(read,1))
                            Wsheet.write(count, 1, Rsheet.cell_value(read, 2))
                            Wsheet.write(count,2,str(item_url))
                            count = count+1
                            Wbook.save('product_list.xlsx')


                except:
                    pass
            try:
                last_button = driver.find_elements(By.CLASS_NAME, 'v-pagination__navigation')[-1]
                print(last_button.get_attribute('class'))
                btn_class = last_button.get_attribute('class')
                if '--disabled' in str(btn_class):
                    b = False
                else:
                    last_button.click()
                    print('GOING TO NEXT PAGE')
                    time.sleep(2)
            except:
                pass
                b = False
driver.quit()