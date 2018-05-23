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
    urls = set()

    featured = soup.find('section', class_='featured container clearfix').find(
        'article').find_all('a', class_=None, href=_exclude_video)
    for link in featured:
        urls.add(link.get('href'))

    list_sub_featured = soup.find('ul', id='list_sub_featured').find_all(
        'a', class_=None, href=_exclude_video)
    for link in list_sub_featured:
        urls.add(link.get('href'))

    sidebar_home_1 = soup.find('section', class_='sidebar_home_1').find_all(
        'article', class_='list_news')
    for section in sidebar_home_1:
        links = section.find_all('a', class_=None, href=_exclude_video)
        for link in links:
            if link is not None:
                urls.add(link.get('href'))

    sidebar_home_2 = soup.find('section', class_='sidebar_home_2').find_all(
        'section', class_='box_category clearfix list_title_right')
    for section in sidebar_home_2:
        article = section.find('article', class_='list_news').find('a', class_=None, href=_exclude_video)
        if article is not None:
            urls.add(article.get('href'))
        ul = section.find('ul', class_='list_title').find_all('a', class_=None, href=_exclude_video)
        for link in ul:
            if link is not None:
                urls.add(link.get('href'))

    related_urls = set()
    for url in urls:
        related_urls.update(extract_urls_from_url(url))
    urls.update(related_urls)
    return urls


def extract_urls_from_url(url):
    page = request.urlopen(url)
    if page.code != 200:
        return set()
    soup = BeautifulSoup(page, 'html.parser')

    urls = set()
    list_title = soup.find('ul', class_='list_title')
    if list_title is None:
        return set()
    list_related_news = list_title.find_all('li')
    for li in list_related_news:
        anchor = li.find('a', class_=None, href=_exclude_video)
        if anchor is not None:
            urls.add(anchor.get('href'))

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
    for p in main_content[:3]:
        if p.find('a') is None:
            chunks.append(p.get_text())

    return '\n'.join(chunks)
