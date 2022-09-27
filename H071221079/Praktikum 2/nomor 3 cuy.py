#Tugas Praktikum Pekan 2 nomor 3

print("\n"+30*'==')
print("MENENTUKAN NILAI TERBESAR DARI TIGA NILAI BERBEDA")
print(30*'==')

a = int(input("\n"'Masukkan Nilai A : '))
b = int(input('Masukkan Nilai B : '))
c = int(input('Masukkan Nilai C : '))

if a > b and a > c:
    d = a
elif b > a and b > c:
    d = b
elif c > a and c > b:
    d = c

    
print(d,'adalah nilai terbesar')
