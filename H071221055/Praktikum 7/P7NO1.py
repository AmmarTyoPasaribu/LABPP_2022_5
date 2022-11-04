import re

nilaistring = input('')
#print(len(s))
regex1 =r'[0?2?4?6?8?_?a-z?A-Z?]' 
regex2 =r'[1?3?5?7?9?\s]' 

result1 = re.findall(regex2, nilaistring[0:40]) 
result2 = re.findall(regex1, nilaistring[41:45])
if result1:
    print('false')
    exit()
elif result2: 
    print('false')
    exit()

if len(nilaistring) == 45:
    print('true')
else:
    print('false')

#2222222222aaaaaaaaaa2222222222aaaaaaaaaa13 57
#x4202v2A22A8a6aaaaaa2G2222m222qwertyYuIo1395779
