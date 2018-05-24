from bs4 import BeautifulSoup
import urllib3
import re


http = urllib3.PoolManager()
urllib3.disable_warnings()


def extract_sitemaps():
    req = http.request('GET', 'https://vnexpress.net/sitemap/1000000/sitemap.xml')
    if req.status != 200:
        return []

    soup = BeautifulSoup(req.data, 'xml')

    sitemap_tags = soup.find_all('sitemap')

    sitemaps = []
    for sitemap in sitemap_tags[:10]:
        loc = sitemap.find('loc')
        sitemaps.append(loc.text)
    return sitemaps


def extract_urls_from_sitemap(sitemap_url):
    req = http.request('GET', sitemap_url)
    if req.status != 200:
        return []

    soup = BeautifulSoup(req.data, 'xml')

    urls = []
    url_tags = soup.find_all('url')
    for url in url_tags[:10]:
        loc = url.find('loc')
        urls.append(loc.text)

    return urls


def extract_text_from_url(url):
    req = http.request('GET', url)
    if req.status != 200:
        return ''

    soup = BeautifulSoup(req.data, 'html.parser')

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
