#Tugas Praktikum Pekan 2 nomor 1
print("\n"+30*'==')
print("KONVERSI NILAI ANGKA KE HURUF")
print(30*'==')

a = int(input("\n"'Masukkan Nilai ='))

if a >= 90:
    b = 'A'
elif a >= 80:
    b = 'B'
elif a >= 70:
    b = 'C'
elif a >= 60:
    b = 'D'
elif a >= 50:
    b = 'E'
elif a < 40:
    b = 'F'


print('nilai',a,' = ', b)