import re
import string
from nltk.tokenize import word_tokenize

def preprocess_string(s):
    s = re.sub(r"[^\w\s]", '', s)
    s = re.sub(r"\s+", '', s)
    s = re.sub(r"\d", '', s)
    return s

def preprocess(text):
    tokens = word_tokenize(text)
    tokens = [preprocess_string(w) for w in tokens]
    return [w.lower() for w in tokens if w and w not in string.punctuation]
