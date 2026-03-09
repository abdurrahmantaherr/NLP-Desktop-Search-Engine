# Desktop Search Engine using Inverted Index

This project implements a desktop keyword search engine capable of indexing and retrieving documents from a large collection of text files using an inverted index.

The system was developed as part of an NLP lab assignment and demonstrates core concepts from information retrieval systems.

## Features

- Indexing of 50,000+ text documents
- Text preprocessing (tokenization, normalization)
- Inverted index construction
- Multiple vector representations:
  - Boolean vectors
  - Count / Frequency vectors
  - TF-IDF vectors
- Similarity measures:
  - Inner Product (Dot Product)
  - Cosine Similarity
- Top-k ranked document retrieval
- Phrase query support
- Proximity query support

## Technologies Used

- Python
- Natural Language Processing concepts
- Vector Space Model
- Inverted Index

## System Workflow

1. Preprocess documents (tokenization, lowercase, punctuation removal)
2. Build inverted index from documents
3. Store term frequencies and document mappings
4. Process user queries
5. Rank documents using TF-IDF and cosine similarity

## Example Query
Query: machine learning
Mode: cosine

Rank | File Path | Score
1 | dataset/doc_3245.txt | 0.92
2 | dataset/doc_7811.txt | 0.89
3 | dataset/doc_2230.txt | 0.87


## Learning Outcomes

Through this project, I gained hands-on experience with:

- Information Retrieval systems
- Vector Space Models
- Search engine indexing techniques
- Document ranking algorithms

## Author

Abdurrahman Tahir
NLP Lab Project
