import nltk, re

sample = open('sample.txt')
text = sample.read()
result = re.findall('[\w\.-]+@[\w\.-]+', text)
print(result)

# '(\w+[.|\w])*@(\w+[.])*\w+'
# '[\w\.-]+@[\w\.-]+'
