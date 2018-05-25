from crawlers.vnexpress import helpers
from crawlers import common


def crawl():
    sitemap_url = 'https://vnexpress.net/sitemap/1000000/sitemap.xml'
    sitemaps = common.extract_sitemaps(sitemap_url)
    for sitemap in sitemaps:
        urls = common.extract_urls_from_sitemap(sitemap)
        for url in urls:
            text = helpers.extract_text_from_url(url)
            yield url, text
