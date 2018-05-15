from crawlers.vnexpress import helpers


class TestHelpers(object):
    def test_extract_urls(self):
        urls = helpers.extract_urls()
        print(urls)

    def test_extract_text_from_url(self):
        url = 'https://vnexpress.net/tin-tuc/phap-luat/canh-sat-vay-bat-nghi-can-dam-chet-2-hiep-si-o-sai-gon-3749303.html'
        text = helpers.extract_text_from_url(url)
        print(text)
