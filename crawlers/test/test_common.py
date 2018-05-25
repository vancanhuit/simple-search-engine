from crawlers import common


class TestCommon(object):
    def test_extract_sitemaps(self):
        sitemap_url = 'https://vnexpress.net/sitemap/1000000/sitemap.xml'
        sitemaps = common.extract_sitemaps(sitemap_url)
        assert len(sitemaps) == 10
        for sitemap in sitemaps:
            print(sitemap)

    def test_extract_urls_from_sitemap(self):
        sitemap_url = 'https://vnexpress.net/sitemap/1000000/sitemap-news.xml?y=2018&m=05&d=25'
        urls = common.extract_urls_from_sitemap(sitemap_url)
        assert len(urls) == 10
        for url in urls:
            print(url)
