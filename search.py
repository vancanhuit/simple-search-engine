import sys
import shelve
import pickle
import os
import math
from utils import helper, textprocessing
from collections import Counter


# Load data from files
db_file = os.path.join(os.getcwd(), 'db', 'index.db')
urls_file = os.path.join(os.getcwd(), 'db', 'urls.db')
stopwords_file = os.path.join(os.getcwd(), 'vietnamese-stopwords.txt')

index_db = shelve.open(db_file)
with open(urls_file, mode='rb') as f:
    urls = pickle.load(f)

with open(stopwords_file, mode='r', encoding='utf-8') as f:
    stopwords_set = set(f.read().split())

# Fetch query and preprocessing
vocabulary = set(index_db.keys())
query = sys.argv[1]
tokens = textprocessing.preprocess_text(query, stopwords_set)
tokens = [token for token in tokens if token in vocabulary]

bow = Counter(tokens)
for term, value in bow.items():
    bow[term] = index_db[term]['idf'] * (1 + math.log(value))
helper.normalize(bow)

# Compute scores
scores = [[i, 0] for i in range(len(urls))]
for term, value in bow.items():
    for index, weight in index_db[term]['postings_list']:
        scores[index][1] += weight * value

scores.sort(key=lambda t: t[1], reverse=True)
for index, score in enumerate(scores[:10]):
    if score[1] == 0:
        break
    print('{}. {} - {}'.format(index + 1, urls[score[0]], score[1]))

index_db.close()
