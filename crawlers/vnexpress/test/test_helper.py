from crawlers.vnexpress import helper


class TestHelper(object):
    def test_extract_text_from_url(self):
        url = 'https://vnexpress.net/tin-tuc/phap-luat/canh-sat-vay-bat-nghi-can-dam-chet-2-hiep-si-o-sai-gon-3749303.html'
        text = helper.extract_text_from_url(url)
        print(text)
