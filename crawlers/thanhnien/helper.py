import requests
from bs4 import BeautifulSoup


def extract_text_from_url(url):
    res = requests.get(url)
    if res.status_code != 200:
        return ''
    soup = BeautifulSoup(res.text, 'html.parser')
    h1 = soup.find('h1', class_='details__headline')
    h2 = soup.find('div', id='chapeau')
    if (h1 is None) or (h2 is None):
        return ''

    main_content = soup.find('div', id='abody')
    if main_content is None:
        return ''

    chunks = []
    chunks.append(h1.get_text().strip())
    chunks.append(h2.get_text().strip())

    divs = main_content.find_all('div', class_=None)
    for div in divs[:2]:
        chunks.append(div.get_text().strip())

    return '\n'.join(chunks)
