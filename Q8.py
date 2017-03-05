import nltk, re

text = 'Address of the School: The Senior Study 2, Putligarh, GT Road, Amritsar.'
result = re.sub('Road', 'Rd.', text)
print(result)
