def getFPB(x, y):
    if x > y:
        kecil = y
    else:
        kecil = x

    for i in range(1, (kecil + 1)):
        if((x % i == 0) and (y % i == 0)):
            fpb = i
    
    print("FPB (" + str(x) + ", " + str(y) + ") = " + str(fpb))

x = int(input())
y = int(input())

getFPB(x, y)