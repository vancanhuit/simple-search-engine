from utils import textprocessing


class TestTextProcessing(object):
    def test_remove_accents(self):
        text = 'áàảãạ âấầẩẫậ ăẵẳằắặ éèẻẽẹ êếềệểễ íìịỉĩ óòỏõọ ôốồổỗộ ơớờởỡợ úùủũụ ưứừửữự ýỳỵỷỹ'
        new_text = textprocessing.remove_accents(text)
        assert new_text == 'aaaaa aaaaaa aaaaaa eeeee eeeeee iiiii ooooo oooooo oooooo uuuuu uuuuuu yyyyy'
