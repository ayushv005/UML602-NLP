import nltk
from nltk.tokenize import sent_tokenize, word_tokenize

sample = open('sample.txt')
text = sample.read()
#print(sample.read())
sents = sent_tokenize(text)
words = word_tokenize(text)
print(sents)
print(words)
