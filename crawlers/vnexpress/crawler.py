from crawlers.vnexpress import helper
from crawlers import common


def crawl(visited_urls):
    sitemap_url = 'https://vnexpress.net/sitemap/1000000/sitemap.xml'
    sitemaps = common.extract_sitemaps(sitemap_url)
    for sitemap in sitemaps[:2]:
        urls = common.extract_urls_from_sitemap(sitemap)
        for url in urls[:50]:
            if url not in visited_urls:
                visited_urls.add(url)
                text = helper.extract_text_from_url(url)
                yield url, text
