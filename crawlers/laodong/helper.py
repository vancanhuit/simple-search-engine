import requests
from bs4 import BeautifulSoup


def extract_text_from_url(url):
    res = requests.get(url)
    if res.status_code != 200:
        return ''

    soup = BeautifulSoup(res.text, 'html.parser')

    h1 = soup.find('h1')
    h2 = soup.find('p', class_='abs')
    if (h1 is None) or (h2 is None):
        return ''

    chunks = []
    chunks.append(h1.get_text().strip())
    chunks.append(h2.get_text().strip())

    main_content = soup.find('div', class_='article-content')
    if main_content is not None:
        paragraphs = main_content.find_all('p', class_=None)
        for p in paragraphs[:2]:
            chunks.append(p.get_text())

    return '\n'.join(chunks)
