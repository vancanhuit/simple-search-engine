import crawlers.vnexpress.crawler as vnexpress_crawler
from utils import helpers, textprocessing
import os
import shelve
import pickle


def get_corpus(stopwords_set):
    data = vnexpress_crawler.crawl()
    for url, text in data:
        if text != '':
            bow = textprocessing.preprocess_text(text, stopwords_set)
            yield url, bow


stopwords_file = os.path.join(os.getcwd(), 'vietnamese-stopwords.txt')
with open(stopwords_file, mode='r') as f:
    stopwords_set = set(f.read().split())


corpus = get_corpus(stopwords_set)
idf = helpers.compute_idf(corpus)

db_file = os.path.join(os.getcwd(), 'db', 'index.db')
if os.path.exists(db_file):
    os.remove(db_file)
index_db = shelve.open(db_file, writeback=True)

for term, value in idf.items():
    index_db[term] = {}
    index_db[term]['idf'] = value
    index_db[term]['postings_list'] = []

corpus = get_corpus(stopwords_set)
urls = []
for url, bow in corpus:
    urls.append(url)
    index = len(urls) - 1
    helpers.compute_weights(bow, idf)
    helpers.normalize(bow)
    for term, value, in bow.items():
        index_db[term]['postings_list'].append((index, value))
    index_db.sync()

urls_file = os.path.join(os.getcwd(), 'db', 'urls.db')
with open(urls_file, mode='wb') as f:
    pickle.dump(urls, f)

index_db.close()
