from urllib import request
from bs4 import BeautifulSoup


def extract_urls():
    url = 'http://soha.vn'
    page = request.urlopen(url)
    if page.code != 200:
        print('Failed to load page')
        return []

    soup = BeautifulSoup(page, 'html.parser')

    urls = set()

    list_special_news = soup.select_one('#ctl00_ctl00_cphBody_cphBody_ctrHomeHighlight_HlDefault')
    titles = list_special_news.find_all('h3')
    for title in titles:
        anchor = title.find('a')
        link = url + anchor.get('href')
        urls.add(link)

    swiper_wrapper = soup.select_one('#slideMoiNhat > div > ul')
    titles = swiper_wrapper.find_all('h3', class_='title')
    for title in titles:
        anchor = title.find('a')
        link = url + anchor.get('href')
        urls.add(link)

    list_topic_cate = soup.select_one('#leftmedium > ul.list-topic-cate.timeline.epl-listdefault')
    titles = list_topic_cate.find_all('h3')
    for title in titles:
        anchor = title.find('a')
        link = url + anchor.get('href')
        urls.add(link)

    box_news = soup.select_one('#box-focus > div:nth-of-type(1)')
    titles = box_news.find_all('h3', class_='title')
    for title in titles:
        anchor = title.find('a')
        link = url + anchor.get('href')
        urls.add(link)

    list_topic_cate = soup.select_one('#leftmedium2 > ul')
    titles = list_topic_cate.find_all('h3', class_=None)
    for title in titles:
        anchor = title.find('a')
        link = url + anchor.get('href')
        urls.add(link)

    clearfix_mgt10 = soup.select_one('#leftmedium2 > div.clearfix.mgt10')
    anchors = clearfix_mgt10.find_all('a', class_='inner show-popup')
    for anchor in anchors:
        link = url + anchor.get('href')
        urls.add(link)

    clearfix_mgt34 = soup.find_all('div', class_='clearfix mgt34')
    for div in clearfix_mgt34:
        anchors = div.find_all('a', class_='inner show-popup')
        for anchor in anchors:
            link = url + anchor.get('href')
            urls.add(link)

    return urls


def extract_text_from_url(url):
    page = request.urlopen(url)
    if page.code != 200:
        return ''
    soup = BeautifulSoup(page, 'html.parser')
    h1 = soup.find('h1', class_='news-title')
    if h1 is None:
        return ''
    h2 = soup.find('h2', class_='news-sapo')
    if h2 is None:
        return ''
    chunks = []
    chunks.append(h1.get_text())
    chunks.append(h2.get_text())

    news_content = soup.find('div', class_='clearfix news-content').find_all('p')
    for p in news_content[:3]:
        chunks.append(p.get_text())

    return '\n'.join(chunks)
