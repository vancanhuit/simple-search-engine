import crawlers.vnexpress.crawler as vnexpress_crawler
import crawlers.thanhnien.crawler as thanhnien_crawler
import crawlers.vietnamnet.crawler as vietnamnet_crawler
from utils import helper, textprocessing
import os
import shelve
import pickle
from collections import Counter


def get_corpus(dataset, stopwords_set):
    for url, text in dataset:
        if text != '':
            tokens = textprocessing.preprocess_text(text, stopwords_set)
            yield url, Counter(tokens)


def get_corpora(stopwords_set):
    vnexpress_dataset = vnexpress_crawler.crawl()
    thanhnien_dataset = thanhnien_crawler.crawl()
    vietnamnet_dataset = vietnamnet_crawler.crawl()

    yield from get_corpus(vnexpress_dataset, stopwords_set)
    yield from get_corpus(thanhnien_dataset, stopwords_set)
    yield from get_corpus(vietnamnet_dataset, stopwords_set)


stopwords_file = os.path.join(os.getcwd(), 'vietnamese-stopwords-dash.txt')
with open(stopwords_file, mode='r', encoding='utf-8') as f:
    stopwords_set = set(f.read().split())


print('Computing idf values...')
corpus = get_corpora(stopwords_set)
idf = helper.compute_idf(corpus)

print('Indexing...')
db_file = os.path.join(os.getcwd(), 'db', 'index.db')
index_db = shelve.open(db_file, writeback=True, flag='n')

for term, value in idf.items():
    index_db[term] = {}
    index_db[term]['idf'] = value
    index_db[term]['postings_list'] = []

corpus = get_corpora(stopwords_set)
urls = []
for url, bow in corpus:
    urls.append(url)
    index = len(urls) - 1
    helper.compute_weights(bow, idf)
    helper.normalize(bow)
    for term, value, in bow.items():
        index_db[term]['postings_list'].append((index, value))
    index_db.sync()

urls_file = os.path.join(os.getcwd(), 'db', 'urls.db')
with open(urls_file, mode='wb') as f:
    pickle.dump(urls, f)

index_db.close()
print('Done.')
