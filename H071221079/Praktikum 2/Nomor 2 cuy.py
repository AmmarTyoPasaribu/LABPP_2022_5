#Tugas Praktikum Pekan 2 nomor 2

print("\n"+30*'==')
print("MENGHITUNG TOTAL TARIF LISTRIK")
print(30*'==')

a = input("\n"'Masukkan Golongan')
b = float(input('Masukkan Daya'))
c = float(input('Masukkan Pemakaian '))
#d = tarif


if a  == 'R1':
    if b == 900:
        d = 1352
    elif b == 1300:
        d = 1444.70
    elif b == 2200:
        d = 1444.70
elif a == 'R2':
    if b >= 3500 and b <= 5500:
        d = 1699.53
elif a == 'R3':
    if b >= 6600:
        d = 1699.53
elif a == 'B2':
    if b >=6600 and b <= 200000:
        d = 1444.70
elif a == 'B3':
    if b > 200000:
        d = 1114.74
elif a == 'I3':
    if b >= 200000:
        d = 1314.12
elif a == 'P1':
    if b >= 6600 and b <= 200000:
        d = 1523.28
else:
    print('data tidak valid')
    exit()
total = d * c
total = ('jumlah tagihan anda : {:_}'.format(total))
print(total)
# print(total.replace('.',',').replace('_','.'))