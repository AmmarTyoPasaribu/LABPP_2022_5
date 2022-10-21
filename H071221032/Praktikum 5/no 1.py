ma = [[0, 0],
    [0, 0]]
 
mb = [[0, 0],
    [0, 0]]

word = ["1,1", "1,2", "2,1", "2,2"]

indeks = 0
for p in range(2):
    for q in range(2):
        ma[p][q] = int(input("Input nilai matriks pertama index " + word[indeks] + ": "))
        indeks += 1

indeks = 0
for p in range(2):
    for q in range(2):
        mb[p][q] = int(input("Input nilai matriks kedua index " + word[indeks] + ": "))
        indeks += 1

mx = [[0,0],
    [0,0]]

for i in range(2):
    for x in range(2):
        for r in range(2):
            mx[i][x] += ma[i][r] * mb[r][x]

p1 = str(ma[0]).replace("[","| ").replace("]"," |")
p2 = str(mb[0]).replace("[","| ").replace("]"," |")
p3 = str(mx[0]).replace("[","| ").replace("]"," |")
p4 = str(ma[1]).replace("[","| ").replace("]"," |")
p5 = str(mb[1]).replace("[","| ").replace("]"," |")
p6 = str(mx[1]).replace("[","| ").replace("]"," |")

print(p1 + " x " + p2 + " = " + p3)
print(p4 + "   " + p5 + "   " + p6)