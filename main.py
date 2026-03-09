from search_engine import boolean_search, count_search, tfidf_search, cosine_search, phrase_search, proximity_search
import pickle

# load document map
with open("index/doc_map.pkl", "rb") as f:
    doc_map = pickle.load(f)

print("Search Engine Ready")

while True:

    query = input("\nEnter query (or 'exit'): ")

    if query == "exit":
        break

    mode = input("Choose mode (boolean / count / tfidf / cosine): ")

    if mode == "boolean":

        docs = boolean_search(query)

        print("\nRank | File Path")

        for i, doc_id in enumerate(docs, 1):
            print(i, doc_map[doc_id])

    elif mode == "count":

        results = count_search(query)

        print("\nRank | File Path | Score")

        for rank, (doc_id, score) in enumerate(results, 1):
            print(rank, doc_map[doc_id], score)

    elif mode == "tfidf":

        results = tfidf_search(query)

        print("\nRank | File Path | Score")

        for rank, (doc_id, score) in enumerate(results, 1):
            print(rank, doc_map[doc_id], score)

    elif mode == "cosine":

        results = cosine_search(query)

        print("\nRank | File Path | Score")

        for rank, (doc_id, score) in enumerate(results, 1):
            print(rank, doc_map[doc_id], score)

    elif mode == "phrase":

        docs = phrase_search(query)

        for rank, doc_id in enumerate(docs, 1):
            print(rank, doc_map[doc_id])
    
    elif mode == "proximity":

        term1 = input("Term 1: ")
        term2 = input("Term 2: ")
        k = int(input("Distance k: "))

        docs = proximity_search(term1, term2, k)

        for rank, doc_id in enumerate(docs, 1):
            print(rank, doc_map[doc_id])

