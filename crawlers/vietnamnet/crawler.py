from crawlers.vietnamnet import helper
from crawlers import common


def crawl(visited_urls):
    sitemap_url = 'http://vietnamnet.vn/sitemap/sitemap.xml'
    sitemaps = common.extract_sitemaps(sitemap_url)
    for sitemap in sitemaps[1:101]:
        urls = common.extract_urls_from_sitemap(sitemap)
        for url in urls:
            if url not in visited_urls:
                visited_urls.add(url)
                text = helper.extract_text_from_url(url)
                yield url, text
