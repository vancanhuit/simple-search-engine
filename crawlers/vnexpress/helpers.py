from bs4 import BeautifulSoup
import requests


def extract_text_from_url(url):
    res = requests.get(url)
    if res.status_code != 200:
        return ''

    soup = BeautifulSoup(res.text, 'html.parser')

    h1 = soup.find('h1', class_='title_news_detail mb10')
    h2 = soup.find('h2', class_='description')
    if (h1 is None) or (h2 is None):
        return ''

    chunks = []
    chunks.append(h1.get_text().strip())
    chunks.append(h2.get_text().strip())

    main_content = soup.find_all('p', class_='Normal')
    for p in main_content[:2]:
        if p.find('a') is None:
            chunks.append(p.get_text().strip())

    return '\n'.join(chunks)
