import sys
import shelve
import pickle
import os
import math
from utils import helpers, textprocessing


# Load data from files
db_file = os.path.join(os.getcwd(), 'db', 'index.db')
urls_file = os.path.join(os.getcwd(), 'db', 'urls.db')
stopwords_file = os.path.join(os.getcwd(), 'vietnamese-stopwords.txt')

index_db = shelve.open(db_file)
with open(urls_file, mode='rb') as f:
    urls = pickle.load(f)

with open(stopwords_file, mode='r') as f:
    stopwords_set = set(f.read().split())

# Fetch query and preprocessing
query = sys.argv[1]
bow = textprocessing.preprocess_text(query, stopwords_set)
for term, value in bow.items():
    bow[term] = index_db[term]['idf'] * (1 + math.log(value))
helpers.normalize(bow)

# Compute scores
scores = [[i, 0] for i in range(len(urls))]
for term, value in bow.items():
    for index, weight in index_db[term]['postings_list']:
        scores[index][1] += weight * value

scores.sort(key=lambda t: t[1], reverse=True)
for index, score in enumerate(scores[:20]):
    if score[1] == 0:
        break
    print('{}. {} - {}'.format(index, urls[score[0]], score[1]))

index_db.close()
