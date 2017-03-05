import nltk, re

string = (raw_input("Enter a string:\n"))
result = re.search('abbb', string)

if result is None:
    print("String invalid.")
else:
    print(result.group(0))
    print("String Accepted.")
