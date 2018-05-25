from crawlers.thanhnien import helper


class TestHelper(object):
    def test_extract_text_from_url(self):
        url = 'https://thanhnien.vn/thoi-su/pho-chu-tich-vff-nguyen-xuan-gu-phu-nhan-thong-tin-mua-dam-966453.html'
        text = helper.extract_text_from_url(url)
        print(text)
