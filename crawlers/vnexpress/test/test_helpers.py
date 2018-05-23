from crawlers.vnexpress import helpers


class TestHelpers(object):
    def test_extract_urls(self):
        urls = helpers.extract_urls()
        for index, url in enumerate(urls):
            print('{}. {}'.format(index + 1, url))

    def test_extract_urls_from_url(self):
        test_url = 'https://vnexpress.net/tin-tuc/thoi-su/trung-quoc-dang-leo-thang-chien-thuat-gam-nham-bien-dong-3753230.html'
        urls = helpers.extract_urls_from_url(test_url)
        for url in urls:
            print(url)

    def test_extract_text_from_url(self):
        url = 'https://vnexpress.net/tin-tuc/phap-luat/canh-sat-vay-bat-nghi-can-dam-chet-2-hiep-si-o-sai-gon-3749303.html'
        text = helpers.extract_text_from_url(url)
        print(text)
