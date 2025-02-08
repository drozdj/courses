"""Create a bigram matrix using the Berkeley Restaurant Project"""
# https://github.com/wooters/berp-trans/blob/master/transcript.txt
# %%
from collections import Counter
import numpy as np
import pandas as pd
# %%
def create_bigram_matrix(corpus):
    words = corpus.split()
    
    bigram_counts = Counter(zip(words[:-1], words[1:]))

    unique_words = sorted(set(words))
    word_to_index = {word: idx for idx, word in enumerate(unique_words)}

    matrix = np.zeros((len(unique_words), len(unique_words)), dtype=int)

    for (w1, w2), count in bigram_counts.items():
        matrix[word_to_index[w1], word_to_index[w2]] = count

    df = pd.DataFrame(matrix, index=unique_words, columns=unique_words)

    return df
# %%
with open('data/cleaned_further_transcript.txt', 'r') as file:
    corpus = file.read()
# %%
bigram_matrix = create_bigram_matrix(corpus)
# %%
