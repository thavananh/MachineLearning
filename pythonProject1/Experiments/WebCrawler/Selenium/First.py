from selenium import webdriver
from selenium.webdriver.common.by import By
import csv

website = 'https://www.adamchoi.co.uk/overs/detailed'
path = '/usr/bin/chromedriver'

driver = webdriver.Chrome()
driver.get(website)

all_matches_button = driver.find_element(By.XPATH, '//label[@analytics-event="All matches"]')
all_matches_button.click()

matches = driver.find_elements(By.TAG_NAME, 'tr')

date = []
home_team = []
score = []
away_team = []

headers = ['date', 'home_team', 'score', 'away_team']

data_list = []

for match in matches:
    try:
        date = match.find_element(By.XPATH, './td[1]').text
        home_team = match.find_element(By.XPATH, './td[2]').text
        score = match.find_element(By.XPATH, './td[3]').text
        away_team = match.find_element(By.XPATH, './td[4]').text
        print(date, home_team, score, away_team)
        data_list.append([date, home_team, score, away_team])
    except Exception as e:
        continue


with open('adamchoi.csv', 'w', newline='') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(headers)
    for row in data_list:
        # print(row)
        print([item.strip() for item in row])
        writer.writerow([item.strip() for item in row])