from crawlers.vietnamnet import helper
from crawlers import common


def crawl():
    sitemap_url = 'http://vietnamnet.vn/sitemap/sitemap.xml'
    sitemaps = common.extract_sitemaps(sitemap_url)
    for sitemap in sitemaps[1:101]:
        urls = common.extract_urls_from_sitemap(sitemap)
        for url in urls:
            print('URL: {}'.format(url))
            text = helper.extract_text_from_url(url)
            yield url, text
