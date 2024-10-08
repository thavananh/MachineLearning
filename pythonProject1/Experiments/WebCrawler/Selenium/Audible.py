from selenium import webdriver
from selenium.webdriver.common.by import By
import csv

website = 'https://www.audible.com/search'
path = '/usr/bin/chromedriver'

driver = webdriver.Chrome()
driver.get(website)
# driver.maximize_window()

container = driver.find_element(By.CLASS_NAME, 'adbl-impression-container ')
products = container.find_elements(By.XPATH, './/li')

print(products)

for product in products:
    try:
        print(product.find_element(By.XPATH, './/h3[contains(@class, "bc-heading")]').text)
    except Exception as e:
        continue