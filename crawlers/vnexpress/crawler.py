from crawlers.vnexpress import helpers


def crawl():
    urls = helpers.extract_urls()
    for url in urls:
        text = helpers.extract_text_from_url(url)
        yield url, text
