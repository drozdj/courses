#
# ! Replicate the bigram probabilities based on the three-sentence corpus.
# %%
from collections import Counter
# %%
def calculate_bigram_prob(corpus):
    words = corpus.split()

    unigram_counts = Counter(words)
    bigram_counts = Counter(zip(words[:-1], words[1:]))

    bigram_prob = {}
    for (w1, w2), count in bigram_counts.items():
        bigram_prob[(w1, w2)] = round(count / unigram_counts[w1], 2)

    return bigram_prob
# %%
corpus = \
" <s> I am Sam </s> \
    <s> Sam I am </s> \
        <s> I do not like green eggs and ham </s> "
# %%
bigram_prob = calculate_bigram_prob(corpus)
bigram_prob
# %%
bigram_prob