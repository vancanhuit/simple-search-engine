from urllib import request
from bs4 import BeautifulSoup
import re


def _exclude_video(href):
    pattern = re.compile('^https://video')
    return pattern.search(href) is None


def extract_urls():
    page = request.urlopen('https://vnexpress.net')
    if page.code != 200:
        print('Failed to load page')
        return []

    soup = BeautifulSoup(page, 'html.parser')

    urls = []

    title_news = soup.find('h1', class_='title_news').find(
        'a', class_=None, href=_exclude_video)
    urls.append(title_news.get('href'))

    list_sub_featured = soup.find('ul', id='list_sub_featured').find_all(
        'a', class_=None, href=_exclude_video)
    for link in list_sub_featured:
        urls.append(link.get('href'))

    sidebar_home_1 = soup.find('section', class_='sidebar_home_1').find_all(
        'article', class_='list_news')
    for article in sidebar_home_1:
        link = article.find('a', class_=None, href=_exclude_video)
        if link is not None:
            urls.append(link.get('href'))

    sidebar_home_2 = soup.find('section', class_='sidebar_home_2').find_all(
        'article', class_='list_news')
    for article in sidebar_home_2:
        link = article.find('a', class_=None, href=_exclude_video)
        if link is not None:
            urls.append(link.get('href'))

    return urls


def extract_text_from_url(url):
    page = request.urlopen(url)
    if page.code != 200:
        return ''

    soup = BeautifulSoup(page, 'html.parser')

    h1 = soup.find('h1', class_='title_news_detail mb10')
    h2 = soup.find('h2', class_='description')
    if (h1 is None) or (h2 is None):
        return ''

    chunks = []
    chunks.append(h1.get_text())
    chunks.append(h2.get_text())

    main_content = soup.find_all('p', class_='Normal')
    for p in main_content:
        if p.find('a') is None:
            chunks.append(p.get_text())

    return '\n'.join(chunks)
