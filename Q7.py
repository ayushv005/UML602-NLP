import nltk, re

text = 'The quick brown fox jumps over the lazy dog.'
result = re.findall("\w*[ae]\w*",text)

for r in result:
    print r
