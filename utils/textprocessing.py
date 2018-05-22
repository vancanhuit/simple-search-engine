import unicodedata
import re
from collections import Counter


def remove_accents(text):
    # https://stackoverflow.com/questions/517923/what-is-the-best-way-to-remove-accents-in-a-python-unicode-string
    return ''.join((c for c in unicodedata.normalize('NFD', text) if unicodedata.category(c) != 'Mn'))


def clean_text(text):
    pattern = pattern = re.compile(r'[^áàảãạâấầẩẫậăẵẳắằặđéèẻẽẹêếềểễệíìịỉĩóòõỏọôốồổộỗơớờởỡợúùũủụưứừửữựýỳỷỹỵ\sa-z]')
    return re.sub(pattern, '', text)


def remove_stopwords(text, stopwords_set):
    tokens = [token for token in text.split() if token not in stopwords_set]
    return tokens


def preprocess_text(text, stopwords_set):
    processed_text = clean_text(text.lower())
    tokens = remove_stopwords(processed_text, stopwords_set)
    tokens = [remove_accents(token) for token in tokens]
    return tokens
