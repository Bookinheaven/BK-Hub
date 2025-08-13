
vocab = {
    "I": 1,
    " love": 2,
    " programming": 3,
    "!": 4
}

# Reverse mapping for decoding 
id_to_token = {v: k for k, v in vocab.items()}

def encode(text : str):
    tokens = []
    for token, token_id in vocab.items():
        count = text.count(token)
        tokens.extend([token_id] * count)
        text = text.replace(token, "", count)
    return tokens

def decode(token_ids):
    return "".join(id_to_token[token_id] for token_id in token_ids)

sentence = "I I love programming! I"
encoded = encode(sentence)
decoded = decode(encoded)

print("Sentence: ", sentence)
print("Encoded: ", encoded)
print("Decoded: ", decoded)