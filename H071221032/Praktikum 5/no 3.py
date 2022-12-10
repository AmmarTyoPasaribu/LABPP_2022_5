a1 = input("Input array ke 1: ").split()
a2 = input("Input array ke 2: ").split()
same = []
x = 0

for i in a2:
    if i in a1:
        i = int(i)
        x += 1
        same += [i]

print("Terdapat", x, "buah duplikat yaitu", tuple(same)) 
