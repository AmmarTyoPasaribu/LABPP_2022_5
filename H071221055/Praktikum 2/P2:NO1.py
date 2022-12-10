from turtle import pen

nilai = int(input('Masukkan nilai 1 - 100:'))
if nilai >= 90 and nilai <= 100:
    print("nilai", nilai, "= 'A'")
elif nilai >= 80 and nilai <= 89:
    print("nilai", nilai, "= 'B'")
elif nilai >= 70 and nilai <= 79:
    print("nilai", nilai, "= 'C'")
elif nilai >= 60 and nilai <= 69:
    print("nilai", nilai, "= 'D'")
elif nilai >= 40 and nilai <= 59:
    print("nilai", nilai, "= 'E'")
elif nilai < 40 and nilai >= 0:
    print("nilai", nilai, "= 'F'")
else:
    print("inputan salah, Masukkan nilai 1 - 100 ")
