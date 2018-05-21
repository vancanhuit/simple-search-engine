from crawlers.soha import helpers


class TestHelpers(object):
    def test_extract_urls(self):
        urls = helpers.extract_urls()
        for index, url in enumerate(urls):
            print('{}. {}'.format(index + 1, url))
