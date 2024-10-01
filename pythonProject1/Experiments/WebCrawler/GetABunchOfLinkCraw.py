from bs4 import BeautifulSoup
import requests
import time
import os  # For handling file paths safely

# Define your custom User-Agent
headers = {
    'User-Agent': 'MyCrawler/1.0 (+http://www.example.com/mycrawler)'
}

website = "https://subslikescript.com/"
response = requests.get(website, headers=headers)
content = response.text

soup = BeautifulSoup(content, 'lxml')

list_li = soup.find_all('li')

for item1 in list_li:
    href = item1.find('a', href=True)
    if href:
        link = href.get('href')
        print(link)
        website1 = "https://subslikescript.com" + link
        try:
            response = requests.get(website1, headers=headers)
            response.raise_for_status()  # Check for HTTP errors
        except requests.exceptions.RequestException as e:
            print(f"An error occurred while requesting {website1}: {e}")
            continue  # Skip to the next item

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
        filepath = os.path.join('transcripts', filename)  # Save all transcripts in a 'transcripts' directory

        # Ensure the directory exists
        os.makedirs(os.path.dirname(filepath), exist_ok=True)

        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(f"Transcript for {title}\n{transcript}")

        print(f"Saved transcript to {filepath}")

        time.sleep(2)  # Be polite and avoid overwhelming the server
