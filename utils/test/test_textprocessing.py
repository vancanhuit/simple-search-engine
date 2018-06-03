from utils import textprocessing


class TestTextProcessing(object):
    def test_remove_accents(self):
        text = 'áàảãạ âấầẩẫậ ăẵẳằắặ đ éèẻẽẹ êếềệểễ íìịỉĩ óòỏõọ ôốồổỗộ ơớờởỡợ úùủũụ ưứừửữự ýỳỵỷỹ'
        new_text = textprocessing.remove_accents(text)
        assert new_text == 'aaaaa aaaaaa aaaaaa d eeeee eeeeee iiiii ooooo oooooo oooooo uuuuu uuuuuu yyyyy'

    def test_clean_text(self):
        text = 'Mỗi lít xăng sẽ chịu thuế môi trường 4.000 đồng còn dầu là 2.000 đồng, cả hai đều là mức cao nhất theo khung hiện hành'
        print(textprocessing.clean_text(text.lower()))

    def test_remove_stopwords(self):
        text = 'ai đó đấy a thủ tướng'
        stopwords_set = {'ai', 'đó', 'đấy', 'a'}
        tokens = textprocessing.remove_stopwords(text, stopwords_set)
        for token in tokens:
            print(token)

    def test_preprocess_text(self):
        text = 'Alô, ai đó và các từ sau đây không phải là stopword'
        stopwords_set = {'ai_đó', 'alô', 'và', 'sau_đây'}
        tokens = textprocessing.preprocess_text(text, stopwords_set)
        print(tokens)
