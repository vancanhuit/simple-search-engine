from crawlers.soha import helpers


class TestHelpers(object):
    def test_extract_urls(self):
        urls = helpers.extract_urls()
        for index, url in enumerate(urls):
            print('{}. {}'.format(index + 1, url))

    def test_extract_urls_from_url(self):
        test_url = 'http://soha.vn/cong-vinh-bi-ong-nguyen-lan-trung-hlv-hai-lo-bat-nat-trong-phut-89-20180523135740518.htm'
        urls = helpers.extract_urls_from_url(test_url)
        for url in urls:
            print(url)

    def test_extract_text_from_url(self):
        url = 'http://soha.vn/vu-bao-hanh-tre-em-o-da-nang-chu-co-so-noi-do-la-phuong-phap-doa-tre-20180521172127597.htm'
        text = helpers.extract_text_from_url(url)
        print(text)
