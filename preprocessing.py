import re

def preprocess(text):
    """
    Convert text into clean tokens.
    """

    # lowercase
    text = text.lower()

    # remove punctuation
    text = re.sub(r'[^a-z0-9\s]', ' ', text)

    # tokenize
    tokens = text.split()

    return tokens