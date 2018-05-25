from collections import defaultdict
import math


def compute_idf(corpus):
    df = defaultdict(lambda: 0)
    num_docs = 0
    for _, doc in corpus:
        num_docs += 1
        for term in doc.keys():
            df[term] += 1

    idf = {}
    for term, value in df.items():
        idf[term] = math.log(num_docs / value)
    return idf


def compute_weights(doc, idf):
    for term, freq in doc.items():
        doc[term] = idf[term] * (1 + math.log(freq))


def normalize(doc):
    denominator = math.sqrt(sum(e ** 2 for e in doc.values()))
    for term, weight in doc.items():
        doc[term] = weight / denominator
