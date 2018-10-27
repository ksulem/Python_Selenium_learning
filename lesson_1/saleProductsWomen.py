import os
from selenium import webdriver

# get the path of chromedriver
dir = os.path.dirname(__file__)
chrome_driver_path = dir + '\chromedriver.exe'
#remove the .exe extension on linux or mac platform

# create a new Chrome session
driver = webdriver.Chrome(chrome_driver_path)
driver.implicitly_wait(30)
driver.maximize_window()

# navigate to the application home page
driver.get('http://demo-store.seleniumacademy.com/')

# find the sale tab
sale_tab = driver.find_element_by_xpath('//*[@id="nav"]/ol/li[5]/a')
sale_tab.click()

# get all the anchor elements which have product names displayed
# currently on result page using find_elements_by_xpath method
products = driver.find_elements_by_xpath("//h2[@class='product-name']/a")

# get the number of anchor elements found
print('Found ' + str(len(products)) + ' products:')

# iterate through each anchor element and
# print the text that is name of the product
for product in products:
    print(product.text)

# close the browser window
driver.quit()