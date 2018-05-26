from crawlers.vietnamnet import helper


class TestHelper(object):
    def test_extract_text_from_url(self):
        url = 'http://vietnamnet.vn/vn/the-gioi/trump-ong-trump-bat-thinh-linh-doi-giong-ve-trieu-tien-453221.html'
        text = helper.extract_text_from_url(url)
        print(text)
