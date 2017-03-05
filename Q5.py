import nltk, re

#string = (raw_input("Enter a string:\n"))
string = "The IP Address is : 192.021.031.908"
result = re.search('(\d){,3}\.(\d){,3}\.(\d){,3}\.(\d){,3}', string)
final_result = re.sub('\.[0]*', '.', result.group(0))

if result is None:
    print("String invalid.")
else:
    print(result.group(0))
    print("String Accepted.")

print("Final Result:  "+ final_result)
