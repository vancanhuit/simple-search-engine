from bs4 import BeautifulSoup
import requests


def extract_sitemaps(sitemap_url):
    res = requests.get(sitemap_url)
    if res.status_code != 200:
        return []

    soup = BeautifulSoup(res.text, 'xml')

    sitemap_tags = soup.find_all('sitemap')

    sitemaps = []
    for sitemap in sitemap_tags:
        loc = sitemap.find('loc')
        sitemaps.append(loc.text)
    return sitemaps


def extract_urls_from_sitemap(sitemap_url):
    res = requests.get(sitemap_url)
    if res.status_code != 200:
        return []

    soup = BeautifulSoup(res.text, 'xml')

    urls = []
    url_tags = soup.find_all('url')
    for url in url_tags:
        loc = url.find('loc')
        urls.append(loc.text)

    return urls
