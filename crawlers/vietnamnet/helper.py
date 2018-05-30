import requests
from bs4 import BeautifulSoup


def extract_text_from_url(url):
    res = requests.get(url)
    if res.status_code != 200:
        return ''

    soup = BeautifulSoup(res.text, 'html.parser')
    h1 = soup.find('h1', class_='title')
    if h1 is None:
        return ''

    main_content = soup.find_all('p', class_='t-j')
    chunks = []
    chunks.append(h1.get_text().strip())
    for p in main_content[:2]:
        chunks.append(p.get_text().strip())

    return '\n'.join(chunks)
