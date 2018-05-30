from collections import defaultdict
import math


def tf(freq):
    return 1 + math.log(freq)


def idf(df, num_docs):
    return math.log(num_docs / df)


def build_inverted_index(urls, corpora, index_db):
    for url, bow in corpora:
        urls.append(url)
        index = len(urls) - 1

        for term, freq in bow.items():
            if index_db.get(term, None) is None:
                index_db[term] = {}

            if index_db[term].get('df', None) is None:
                index_db[term]['df'] = 0

            if index_db[term].get('postings_list', None) is None:
                index_db[term]['postings_list'] = {}

            index_db[term]['df'] += 1
            index_db[term]['postings_list'][index] = freq

            index_db.sync()

        index_db.sync()
