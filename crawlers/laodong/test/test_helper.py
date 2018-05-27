from crawlers.laodong import helper


class TestHelper(object):
    def test_extract_text_from_url(self):
        url = 'https://laodong.vn/phap-luat/xet-xu-tai-bien-chay-than-cang-ve-cuoi-cang-gay-can-609482.ldo'
        text = helper.extract_text_from_url(url)
        print(text)
