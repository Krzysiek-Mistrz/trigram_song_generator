from model.tokenizer import preprocess
from model.ngram_model import build_trigram_model, predict_next

def generate_text(text, length=100):
    tokens = preprocess(text)
    model = build_trigram_model(tokens)

    w1, w2 = tokens[0], tokens[1]
    output = [w1, w2]

    for _ in range(length):
        next_word = predict_next(model, w1, w2)
        if not next_word:
            break
        output.append(next_word)
        w1, w2 = w2, next_word

    return ' '.join(output)
