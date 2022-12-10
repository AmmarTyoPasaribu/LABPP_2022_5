nilai = int(input('Masukkan angka :'))
n1 = 0
n2 = 1

for i in range(nilai):
    print(n1,end =' ')
    angka_selanjutnya = n1 + n2
    n1 = n2
    n2 = angka_selanjutnya
print()