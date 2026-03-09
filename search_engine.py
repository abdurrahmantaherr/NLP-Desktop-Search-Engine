import pickle
import math
from collections import defaultdict
from preprocessing import preprocess

# Load inverted index
with open("index/inverted_index.pkl", "rb") as f:
    inverted_index = pickle.load(f)



# Load document map
with open("index/doc_map.pkl", "rb") as f:
    doc_map = pickle.load(f)

N = len(doc_map)


def compute_idf(term):
    df = len(inverted_index.get(term, []))
    return math.log((N + 1) / (df + 1)) + 1

# Precompute document vector norms for cosine similarity

doc_norms = defaultdict(float)

for term, postings in inverted_index.items():

    idf = compute_idf(term)

    for doc_id, tf in postings:

        weight = tf * idf
        doc_norms[doc_id] += weight ** 2


# square root of sums
for doc_id in doc_norms:
    doc_norms[doc_id] = math.sqrt(doc_norms[doc_id])


# BOOLEAN SEARCH
def boolean_search(query):

    tokens = preprocess(query)

    results = set()

    for term in tokens:

        if term in inverted_index:

            docs = [doc_id for doc_id, tf in inverted_index[term]]

            results.update(docs)

    return list(results)[:10]


# COUNT VECTOR SEARCH
def count_search(query):

    tokens = preprocess(query)

    scores = defaultdict(int)

    for term in tokens:

        if term not in inverted_index:
            continue

        for doc_id, tf in inverted_index[term]:

            scores[doc_id] += tf

    ranked = sorted(scores.items(), key=lambda x: x[1], reverse=True)

    return ranked[:10]


# TF-IDF SEARCH
def tfidf_search(query):

    tokens = preprocess(query)

    scores = defaultdict(float)

    for term in tokens:

        if term not in inverted_index:
            continue

        idf = compute_idf(term)

        for doc_id, tf in inverted_index[term]:

            tfidf = tf * idf

            scores[doc_id] += tfidf

    ranked = sorted(scores.items(), key=lambda x: x[1], reverse=True)

    return ranked[:10]

def cosine_search(query):

    tokens = preprocess(query)

    scores = defaultdict(float)

    query_weights = {}
    query_norm = 0

    # compute query TF-IDF
    for term in tokens:

        idf = compute_idf(term)

        weight = idf
        query_weights[term] = weight

        query_norm += weight ** 2

    query_norm = math.sqrt(query_norm)

    # compute dot product
    for term, q_weight in query_weights.items():

        if term not in inverted_index:
            continue

        idf = compute_idf(term)

        for doc_id, tf in inverted_index[term]:

            d_weight = tf * idf
            scores[doc_id] += d_weight * q_weight

    # normalize by vector norms
    for doc_id in scores:

        scores[doc_id] = scores[doc_id] / (doc_norms[doc_id] * query_norm)

    ranked = sorted(scores.items(), key=lambda x: x[1], reverse=True)

    return ranked[:10]

def phrase_search(query):

    phrase = query.lower().split()

    results = []

    for doc_id, path in doc_map.items():

        try:
            with open(path, "r", encoding="utf-8", errors="ignore") as f:
                text = f.read().lower()

                if " ".join(phrase) in text:
                    results.append(doc_id)

        except:
            continue

    return results[:10]

def proximity_search(term1, term2, k):

    results = []

    for doc_id, path in doc_map.items():

        try:
            with open(path, "r", encoding="utf-8", errors="ignore") as f:
                words = preprocess(f.read())

                positions1 = [i for i,w in enumerate(words) if w == term1]
                positions2 = [i for i,w in enumerate(words) if w == term2]

                for p1 in positions1:
                    for p2 in positions2:

                        if abs(p1 - p2) <= k:
                            results.append(doc_id)
                            break

        except:
            continue

    return results[:10]