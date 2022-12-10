angka_1 = int(input('a:'))
angka_2 = int(input('b:'))
angka_3 = int(input('c:'))

if angka_1 > angka_2 and angka_1 > angka_3:
    print(angka_1, "adalah angka terbesar")
elif angka_2 > angka_1 and angka_2 > angka_3:
    print(angka_2, "adalah angka terbesar")
else:
    print(angka_3, "adalah angka terbesar")
