import re

file = open("empasslist.txt", "ra")
string = file.read()
print(string)
# x = re.match("a@a.com", string)
# print("true") if x else print("false")
