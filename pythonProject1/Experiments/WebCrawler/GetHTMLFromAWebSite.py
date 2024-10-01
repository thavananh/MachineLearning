from bs4 import BeautifulSoup
import requests

website = 'https://subslikescript.com/movie/Titanic-120338'
response = requests.get(website)
content = response.text

soup = BeautifulSoup(content, 'lxml')
# print(soup.prettify())

box = soup.find('article', claass_= 'main-article')

title = soup.find('h1').get_text()
print(title)

transcript = soup.find('div', class_='full-script').get_text(strip=True, separator=' ')
print(transcript)

with open('transcript.txt', 'w', encoding='utf-8') as f:
    f.write(transcript)