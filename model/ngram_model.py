import nltk
from collections import defaultdict

def build_trigram_model(tokens):
    trigrams = nltk.trigrams(tokens)
    model = defaultdict(lambda: defaultdict(int))
    for w1, w2, w3 in trigrams:
        model[(w1, w2)][w3] += 1
    return model

def predict_next(model, w1, w2):
    options = model.get((w1, w2), {})
    if not options:
        return None
    sorted_options = sorted(options.items(), key=lambda x: x[1], reverse=True)
    return sorted_options[0][0]
