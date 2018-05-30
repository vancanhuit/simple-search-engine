from crawlers.laodong import helper
from crawlers import common


def crawl(visited_urls):
    sitemap_url = 'https://laodong.vn/sitemap.xml'
    sitemaps = common.extract_sitemaps(sitemap_url)

    for sitemap in sitemaps[:10]:
        urls = common.extract_urls_from_sitemap(sitemap)
        for url in urls[:10]:
            if url not in visited_urls:
                visited_urls.add(url)
                text = helper.extract_text_from_url(url)
                yield url, text
