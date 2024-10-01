from time import sleep

from bs4 import BeautifulSoup
import requests
import time
import os  # For handling file paths safely

# Define your custom User-Agent
headers = {
    'User-Agent': 'MyCrawler/1.0'
}

website = "https://subslikescript.com/movies?page=1"
response = requests.get(website, headers=headers)
content = response.text

soup = BeautifulSoup(content, 'lxml')

box = soup.find('article', class_='main-article')
list_li = box.find_all('li')

pagination_links = soup.find('ul', class_='pagination').find_all('a')

max_element = -1
for item in pagination_links:
    print(item.get_text())
    try:
        if max_element < int(item.get_text()):
            max_element = int(item.get_text())
    except ValueError:
        continue

print(max_element)

for i in range(1, 10 + 1):
    website = "https://subslikescript.com/movies?page=" + str(i)
    response = requests.get(website, headers=headers)
    content = response.text
    soup = BeautifulSoup(content, 'lxml')
    box = soup.find('article', class_='main-article')
    list_li = box.find_all('li')

    for item1 in list_li:
        href = item1.find('a', href=True)
        if href:
            link = href.get('href')
            print(link)
            website1 = "https://subslikescript.com/" + link
            try_count = 1
            while try_count <= 3:
                try:
                    response = requests.get(website1, headers=headers)
                    response.raise_for_status()  # Check for HTTP errors
                    break
                except requests.exceptions.RequestException as e:
                    print(f"An error occurred while requesting {website1}: {e}")
                    print(f"The program will auto try again the link 3 times or it will skip: {try_count}")
                    try_count += 1  # Skip to the next item
                    if try_count == 3:
                        continue
                    sleep(2)

            content = response.text
            soup = BeautifulSoup(content, 'lxml')

            title_element = soup.find('h1')
            if title_element:
                title = title_element.get_text()
            else:
                print(f"Title not found for {website1}")
                continue

            transcript_element = soup.find('div', class_='full-script')
            if transcript_element:
                transcript = transcript_element.get_text(strip=True, separator=' ')
            else:
                print(f"Transcript not found for {website1}")
                continue

            # Clean up the title to use it as a filename
            safe_title = ''.join(c for c in title if c.isalnum() or c in (' ', '_', '-')).rstrip()
            filename = f"transcript_{safe_title}.txt"
            filepath = os.path.join('transcripts_2', filename)  # Save all transcripts in a 'transcripts' directory

            # Ensure the directory exists
            os.makedirs(os.path.dirname(filepath), exist_ok=True)

            with open(filepath, 'w', encoding='utf-8') as f:
                f.write(f"Transcript for {title}\n{transcript}")

            print(f"Saved transcript to {filepath}")

            time.sleep(2)  # Be polite and avoid overwhelming the server
