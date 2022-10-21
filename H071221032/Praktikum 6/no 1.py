x = input() + ".txt"
file1 = open(x, "r")
a = file1.read()

y = input() + ".txt"

file2 = open(y, "w")
file2.write(a)

try:
    test = open(y, "r")
except:
    print("Gagal")

file1.close()
file2.close()