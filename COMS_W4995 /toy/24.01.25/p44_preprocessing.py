#
# ! Remove the timestamps from data/transcript.txt, and output it to data/cleaned_transcript.txt

"""
Before:
55_1_0010 i want to spend less than five dollars
55_1_0011 [um] i can drive so it can be anywhere
55_1_0012 can you show me th- [uh] more information about

After:
i want to spend less than five dollars
[um] i can drive so it can be anywhere
can you show me th- [uh] more information about international house cafe 
"""
# %%
import re
# %%
def remove_timestamps(corpus):
    pattern = r'\b\w*[A-Z0-9]\w*\b'
    cleaned_lines = [re.sub(pattern, '', line).strip() for line in corpus.split('\n') if line.strip()]
    return '\n'.join(cleaned_lines)
# %%
with open('data/transcript.txt', 'r') as file:
    corpus = file.read()
# %%
cleaned_corpus = remove_timestamps(corpus)
# %% 
with open('data/cleaned_transcript.txt', 'w') as file:
    file.write(cleaned_corpus)