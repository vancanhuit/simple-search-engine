import crawlers.vnexpress.crawler as vnexpress_crawler
import crawlers.thanhnien.crawler as thanhnien_crawler
import crawlers.vietnamnet.crawler as vietnamnet_crawler
import crawlers.laodong.crawler as laodong_crawler
from utils import helper, textprocessing
import os
import shelve
import pickle
from collections import Counter
import math


def get_corpus(dataset, stopwords_set):
    for url, text in dataset:
        if text != '':
            tokens = textprocessing.preprocess_text(text, stopwords_set)
            print('URL: {}'.format(url))
            yield url, Counter(tokens)


def get_corpora(stopwords_set):
    vnexpress_dataset = vnexpress_crawler.crawl()
    thanhnien_dataset = thanhnien_crawler.crawl()
    vietnamnet_dataset = vietnamnet_crawler.crawl()
    laodong_dataset = laodong_crawler.crawl()

    yield from get_corpus(vnexpress_dataset, stopwords_set)
    yield from get_corpus(thanhnien_dataset, stopwords_set)
    yield from get_corpus(vietnamnet_dataset, stopwords_set)
    yield from get_corpus(laodong_dataset, stopwords_set)


stopwords_file = os.path.join(os.getcwd(), 'vietnamese-stopwords-dash.txt')
with open(stopwords_file, mode='r', encoding='utf-8') as f:
    stopwords_set = set(f.read().split())

urls_file = os.path.join(os.getcwd(), 'db', 'urls.db')
lengths_file = os.path.join(os.getcwd(), 'db', 'lengths.db')
index_db_file = os.path.join(os.getcwd(), 'db', 'index.db')

corpora = get_corpora(stopwords_set)
urls = []

index_db = shelve.open(index_db_file, flag='n', writeback=True)
# Build inverted index
helper.build_inverted_index(urls, corpora, index_db)

# Caculate lengths for normalizing
num_docs = len(urls)
lengths = [0 for i in range(num_docs)]
for index in range(num_docs):
    # Re-construct doc vector from inverted index
    vector = []
    for term, value in index_db.items():
        df = value['df']
        postings_list = value['postings_list']

        if index in postings_list.keys():
            weight = helper.tf(postings_list[index]) * helper.idf(df, num_docs)
            vector.append(weight)

    lengths[index] = math.sqrt(sum((e ** 2 for e in vector)))

index_db.close()

with open(urls_file, mode='wb') as f:
    pickle.dump(urls, f)
with open(lengths_file, mode='wb') as f:
    pickle.dump(lengths, f)
