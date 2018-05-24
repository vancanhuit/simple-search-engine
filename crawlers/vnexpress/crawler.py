from crawlers.vnexpress import helpers


def crawl():
    sitemaps = helpers.extract_sitemaps()
    for sitemap in sitemaps:
        urls = helpers.extract_urls_from_sitemap(sitemap)
        for url in urls:
            text = helpers.extract_text_from_url(url)
            yield url, text
