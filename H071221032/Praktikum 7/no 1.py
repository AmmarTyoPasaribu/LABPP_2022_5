import re

StringS = input()
pattern0 = "^.{45}"
pattern1 = "^([a-zA-Z]|(0|2|4|6|8))+"
pattern2 = "(( )|(1|3|5|7|9))+$"

result0 = re.search(pattern0, StringS)
result1 = re.search(pattern1, StringS)
result2 = re.search(pattern2, StringS)

if result0.span() == (0,45):
    if result1.span() == (0,40):
        if result2.span() == (40,45):
            print("true")
            exit()
print("false")

