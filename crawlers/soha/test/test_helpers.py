from crawlers.soha import helpers


class TestHelpers(object):
    def test_extract_urls(self):
        urls = helpers.extract_urls()
        for index, url in enumerate(urls):
            print('{}. {}'.format(index + 1, url))

    def test_extract_text_from_url(self):
        url = 'http://soha.vn/vu-bao-hanh-tre-em-o-da-nang-chu-co-so-noi-do-la-phuong-phap-doa-tre-20180521172127597.htm'
        text = helpers.extract_text_from_url(url)
        print(text)
