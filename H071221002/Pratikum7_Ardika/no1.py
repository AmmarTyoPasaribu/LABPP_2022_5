import re

try:
    string_s = input("masukkan String S: ")
    pattern = re.fullmatch("[2468a-zA-Z]{40}[13579\s]{5}", string_s)
    if pattern :
        print("True")
    else:
        print("False")
except:
    print("False")