def take_FPB(x, y):
    if x>y:
        terbesar = x
    else:
        terbesar = y
    for i in range(1, terbesar + 1):
        x % i == 0 and y % i == 0
        fpb = i
        return fpb

bil1 = int(input())
bil2 = int(input())

print("FPB({},{})={}".format (bil1, bil2, take_FPB(bil1,bil2)))