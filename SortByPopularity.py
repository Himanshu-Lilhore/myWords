import nltk
from nltk.corpus import brown

# wordlist = ["corpus", "house", "the", "Peter", "asdf"]
# # collect frequency information from brown corpus, might take a few seconds
# freqs = nltk.FreqDist([w.lower() for w in brown.words()])
# # sort wordlist by word frequency
# wordlist_sorted = sorted(
#     wordlist, key=lambda x: freqs[x.lower()], reverse=True)
# # print the sorted list
# for w in wordlist_sorted:
#     print(w)

help(nltk.corpus.brown)
