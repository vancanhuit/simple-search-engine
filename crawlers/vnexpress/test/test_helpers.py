from crawlers.vnexpress import helpers


class TestHelpers(object):
    def test_extract_sitemaps(self):
        sitemaps = helpers.extract_sitemaps()
        assert len(sitemaps) == 10
        for sitemap in sitemaps:
            print(sitemap)

    def test_extract_urls_from_sitemap(self):
        sitemap_url = 'https://vnexpress.net/sitemap/1000000/sitemap-news.xml?y=2018&m=05&d=24'
        urls = helpers.extract_urls_from_sitemap(sitemap_url)
        assert len(urls) == 10
        for url in urls:
            print(url)

    def test_extract_text_from_url(self):
        url = 'https://vnexpress.net/tin-tuc/phap-luat/canh-sat-vay-bat-nghi-can-dam-chet-2-hiep-si-o-sai-gon-3749303.html'
        text = helpers.extract_text_from_url(url)
        print(text)
