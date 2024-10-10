from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service
from seleniumbase import Driver
import csv

options = Options()
options.add_argument("--window-size=1920x1080")
# options.add_argument("--headless")

website = 'https://www.audible.com/search'

driver = Driver(uc = True, browser="chrome", locale_code='vi', )
driver.maximize_window()

driver.uc_open_with_reconnect(website, 4)
driver.uc_gui_click_captcha()


wait = WebDriverWait(driver, 10)

pagination = wait.until(EC.presence_of_element_located((By.XPATH, '//ul[contains(@class, "pagingElements")]')))
pages = pagination.find_elements(By.XPATH, './li')
print(pages[len(pages)-2].text)

last_page = int(pages[len(pages)-2].text)

# Wait for the container to be present


data_list = []

current_page = 1

while current_page <= last_page:
    container = wait.until(EC.presence_of_element_located((By.CLASS_NAME, 'adbl-impression-container ')))

    # Find the product elements
    products = container.find_elements(By.XPATH, './/li[contains(@class, "productListItem")]')
    for product in products:
        title = product.find_element(By.XPATH, './/h3[contains(@class, "bc-heading")]').text
        author = product.find_element(By.XPATH, './/li[contains(@class, "authorLabel")]').text
        runtime = product.find_element(By.XPATH, './/li[contains(@class, "runtimeLabel")]').text

        print(title)
        print(author)
        print(runtime)

        data_list.append([title, author, runtime])
    next_page = driver.find_element(By.XPATH, './/span[contains(@class, "nextButton")]')
    next_page.click()
    current_page += 1

headers = ['Title', 'Author', 'Length']

with open('outputAudible.csv', 'w', newline='', encoding='utf-8') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(headers)
    for row in data_list:
        writer.writerow([item.strip() if isinstance(item, str) else item for item in row])

driver.quit()
