import unicodedata
import re
from collections import Counter
from underthesea import word_tokenize


def remove_accents(text):
    # https://stackoverflow.com/questions/517923/what-is-the-best-way-to-remove-accents-in-a-python-unicode-string
    no_accents_text = ''.join((c for c in unicodedata.normalize('NFD', text) if unicodedata.category(c) != 'Mn'))
    return no_accents_text.replace('đ', 'd')


def clean_text(text):
    pattern = pattern = re.compile(r'[^áàảãạâấầẩẫậăẵẳắằặđéèẻẽẹêếềểễệíìịỉĩóòõỏọôốồổộỗơớờởỡợúùũủụưứừửữựýỳỷỹỵ\sa-z_]')
    return re.sub(pattern, ' ', text)


def remove_stopwords(text, stopwords_set):
    tokens = [token for token in text.split() if token not in stopwords_set]
    return tokens


def preprocess_text(text, stopwords_set):
    processed_text = word_tokenize(text, format='text')
    processed_text = processed_text.lower()
    processed_text = clean_text(processed_text)
    tokens = remove_stopwords(processed_text, stopwords_set)
    tokens = [remove_accents(token) for token in tokens]
    return tokens
