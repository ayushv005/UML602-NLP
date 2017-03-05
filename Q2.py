import nltk, re

string = (raw_input("Enter a string:\n"))
result = re.search('[A-Za-z0-9]$', string)
#print(result.group(0))

if result is None:
    print("String invalid.")
else:
    print("String Accepted.")
