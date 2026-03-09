import os
from collections import defaultdict, Counter
from preprocessing import preprocess
import pickle


def get_all_files(folder):
    files = []

    for root, dirs, filenames in os.walk(folder):
        for file in filenames:
            if file.endswith(".txt"):
                files.append(os.path.join(root, file))

    return files

def build_index(dataset_path):

    inverted_index = defaultdict(list)
    doc_map = {}

    files = get_all_files(dataset_path)

    for doc_id, file_path in enumerate(files):

        doc_map[doc_id] = file_path

        try:
            with open(file_path, "r", encoding="utf-8", errors="ignore") as f:
                text = f.read()
        except:
            continue

        tokens = preprocess(text)

        term_freq = Counter(tokens)

        for term, freq in term_freq.items():
            inverted_index[term].append((doc_id, freq))

    return inverted_index, doc_map

def save_index(index, doc_map):

    os.makedirs("index", exist_ok=True)

    with open("index/inverted_index.pkl", "wb") as f:
        pickle.dump(index, f)

    with open("index/doc_map.pkl", "wb") as f:
        pickle.dump(doc_map, f)
    
    