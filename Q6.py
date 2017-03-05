import nltk, re

pattern = [ 'fox', 'dog', 'horse' ]
text = 'The quick brown fox jumps over the lazy dog.'

for x in pattern:
    print("Searching for '"+x+"' in the given text:")
    if re.search(x,  text):
        print('Matched!')
    else:
        print('Not Matched!')
