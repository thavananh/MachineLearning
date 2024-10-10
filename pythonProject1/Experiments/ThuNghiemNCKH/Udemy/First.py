from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service
from seleniumbase import Driver
import time
import pandas as pd

options = Options()
options.add_argument("start-maximized")
options.add_experimental_option("excludeSwitches", ["enable-automation"])
options.add_experimental_option('excludeSwitches', ['enable-logging'])
options.add_experimental_option('useAutomationExtension', False)
options.add_argument('--disable-blink-features=AutomationControlled')

#//div[contains(@id, 'course-unit-container-Hcvinangxem')]//div[@data-testid='course-details-popover-trigger']

website = 'https://www.udemy.com'

driver = Driver(uc=True, browser="chrome", locale_code='vi', )
driver.maximize_window()

driver.uc_open_with_reconnect(website, 4)
driver.uc_gui_click_captcha()

ui_change = True

try:
    next_button = driver.find_element(By.XPATH,
                                      '(//div[@class="component-margin"])[1]//button[@data-pager-type="next"]')  #auto xpath generate
except Exception as e:
    next_button = driver.find_element(By.XPATH, '//section[@id="discovery-units-top"]//button[@data-pager-type="next"]')
    ui_change = False

while next_button.is_displayed():
    next_button.click()
    time.sleep(3)

course_carousel = driver.find_elements(By.XPATH, '(//div[@class="component-margin"])[1]//div[@data-index]')

if len(course_carousel) == 0:
    course_carousel = driver.find_elements(By.XPATH, '//section[@id="discovery-units-top"]//div[@data-index]')

links = []

for item in course_carousel:


    if ui_change:
        href = item.find_element(By.XPATH, './/a')  #auto xpath generate
    else:
        href = item.find_element(By.XPATH, './/a')  # auto xpath generate

    links.append(href.get_attribute('href'))

for item in links:
