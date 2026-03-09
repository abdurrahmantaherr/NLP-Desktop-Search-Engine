import os
import random

topics = [
    "machine learning and artificial intelligence",
    "natural language processing and text mining",
    "cricket world cup and pakistan cricket team",
    "data science and big data analytics",
    "computer networks and cybersecurity",
    "deep learning neural networks",
    "information retrieval and search engines",
    "software engineering and programming",
    "database systems and sql queries",
    "cloud computing and distributed systems"
]

os.makedirs("dataset", exist_ok=True)

NUM_FILES = 50000

for i in range(NUM_FILES):

    file_path = f"dataset/doc_{i}.txt"

    text = " ".join(random.choices(topics, k=20))

    with open(file_path, "w") as f:
        f.write(text)

print("50,000 files generated successfully.")